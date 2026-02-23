import os
import json
import groq

client = groq.Client(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_transcript(text):

    prompt = f"""
    You are a senior equity research analyst.

    Your task is to carefully extract structured insights from the earnings call transcript.

    IMPORTANT:
    - Read the entire transcript carefully.
    - Extract as much relevant financial and operational insight as possible.
    - Avoid returning empty fields unless absolutely necessary.
    - If evidence exists but is indirect, classify cautiously instead of writing "Not Mentioned".

    Return ONLY valid JSON in the format below:

    {{
    "management_tone": {{
        "classification": "",
        "confidence_level": "",
        "supporting_quotes": []
    }},
    "key_positives": [],
    "key_concerns": [],
    "forward_guidance": {{
        "revenue": "",
        "margin": "",
        "capex": ""
    }},
    "operational_indicators": {{
        "capacity_utilization": ""
    }},
    "new_growth_initiatives": []
    }}

    Rules:
    - Extract 3–5 positives if possible.
    - Extract 3–5 concerns if possible.
        - Use direct quotes when available.

    Forward Guidance Handling:
    - If numeric guidance is provided (%, range, revenue amount), extract it clearly.
    - If directional guidance is provided (e.g., "expect improvement", "margin expansion", "growth next year"), summarize the direction qualitatively.
    - Treat phrases like "expect", "outlook", "forecast", "next quarter", "next year", "should improve", "will normalize", "planned capex" as forward-looking guidance.
    - Only write "Not Mentioned" if there is absolutely no forward-looking commentary.

Never invent numbers or precision that is not explicitly stated.

    Transcript:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a precise financial analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        generated_text = response.choices[0].message.content

        # Extract JSON safely
        start = generated_text.find("{")
        end = generated_text.rfind("}") + 1

        if start == -1 or end == -1:
            return {"error": "No valid JSON found in model output"}

        json_text = generated_text[start:end]

        return json.loads(json_text)

    except Exception as e:
        return {"error": str(e)}