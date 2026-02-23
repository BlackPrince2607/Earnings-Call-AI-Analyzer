📊 Earnings Call AI Analyzer

Deployed Here: https://earnings-call-summary-portal.onrender.com

An AI-powered financial transcript analyzer that extracts structured insights from earnings call PDFs using Large Language Models.

Deployed on Render.

🚀 Overview

This application allows users to upload an earnings call transcript (PDF) and automatically generates structured financial insights including:

Management Tone Classification

Key Positives

Key Concerns

Forward Guidance (Revenue, Margin, Capex)

Operational Indicators

New Growth Initiatives

The system is built using FastAPI and integrates with an LLM for structured financial analysis.

🧠 Features

📄 PDF Upload & Text Extraction (pdfplumber)

🧠 AI-Powered Financial Insight Extraction

📊 Structured JSON Output

🎯 Hallucination-Reduced Prompt Design

🖥 Clean Corporate UI (Jinja2 Templates)

☁️ Cloud Deployment (Render)

🏗 Tech Stack

Backend

FastAPI

Uvicorn

Jinja2

pdfplumber

AI Layer

Groq LLM (LLaMA 3.1 8B Instant)

Structured Prompt Engineering

JSON Output Enforcement

Deployment

Render (Python 3.11)

📂 Project Structure
├── main.py              # FastAPI routes
├── analyser.py          # AI analysis logic
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md
🔎 How It Works

User uploads an earnings call PDF.

Text is extracted using pdfplumber.

Transcript is passed to an LLM with a structured extraction prompt.

Model returns JSON-formatted financial insights.

Results are rendered in a clean corporate UI.

🛡 Hallucination Control

To reduce hallucinations:

The prompt explicitly instructs the model to:

Use only transcript evidence

Provide supporting quotes

Avoid fabricating numbers

Return "Not Mentioned" only if truly absent

JSON parsing ensures structured output validation.

Errors are handled gracefully in UI.

⚙️ Local Setup
1️⃣ Clone Repository
git clone <your-repo-url>
cd earnings-call-analyzer
2️⃣ Create Virtual Environment
python -m venv .venv

Activate:

Windows

.venv\Scripts\activate

Mac/Linux

source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Environment Variable

Windows

set GROQ_API_KEY=your_api_key_here

Mac/Linux

export GROQ_API_KEY=your_api_key_here
5️⃣ Run Application
uvicorn main:app --reload

Open:

https://earnings-call-summary-portal.onrender.com/
🌐 Deployment

Deployed on Render using:

uvicorn main:app --host 0.0.0.0 --port 10000

Python Version: 3.11
Dependencies pinned for compatibility.

📈 Future Improvements

Chunking for long transcripts

Sentiment scoring meter

Downloadable PDF report

Database storage of analyses

Advanced confidence scoring

🎓 Learning Outcomes

This project demonstrates:

Backend API development (FastAPI)

AI integration and prompt engineering

Structured JSON extraction

Error handling & dependency debugging

Cloud deployment (Render)

Production-level troubleshooting

👨‍💻 Author

Soham Bhalotia
B.Tech CSSE
AI & Financial Analysis Enthusiast