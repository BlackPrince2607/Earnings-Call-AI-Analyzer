import os
import json
from groq import Groq

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_transcript(text):

    prompt = f"""
You are a financial research analyst.

Extract structured insights from the transcript below.

Return ONLY valid JSON in this format:

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
- Do NOT infer missing information.
- If information is not found, write "Not Mentioned".
- Do not include any explanation outside JSON.
- Use only evidence from the transcript.

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