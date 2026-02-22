from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pdfplumber
from analyser import analyze_transcript   # make sure spelling matches your file

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze")
async def analyze(request: Request, file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)   # this needs extract_text defined below
    text = text[:5000]
    print("Extracted length:", len(text))
    result = analyze_transcript(text)

    if "error" in result:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "data": result
            }
        )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "data": result
        }
    )


# 🔥 THIS FUNCTION MUST EXIST
def extract_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text