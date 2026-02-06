
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import re
from typing import List, Dict

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = "demo_api_key_123"   # Change before submission


class ScamMessage(BaseModel):
    message: str


def extract_emails(text: str) -> List[str]:
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)


def extract_urls(text: str) -> List[str]:
    return re.findall(r"https?://[^\s]+", text)


def extract_phone_numbers(text: str) -> List[str]:
    return re.findall(r"(?:\+91|91)?[6-9]\d{9}", text)


def detect_scam_keywords(text: str) -> List[str]:
    keywords = [
        "urgent", "lottery", "prize", "winner", "free",
        "click now", "limited offer", "bank update",
        "otp", "verify account", "investment",
        "crypto", "bitcoin", "gift card"
    ]
    found = [k for k in keywords if k.lower() in text.lower()]
    return found


@app.post("/analyze")
def analyze_message(data: ScamMessage, x_api_key: str = Header(None)):

    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    text = data.message

    intelligence: Dict = {
        "emails": extract_emails(text),
        "urls": extract_urls(text),
        "phone_numbers": extract_phone_numbers(text),
        "scam_keywords": detect_scam_keywords(text),
        "risk_score": 0
    }

    score = 0
    score += len(intelligence["emails"]) * 20
    score += len(intelligence["urls"]) * 20
    score += len(intelligence["phone_numbers"]) * 20
    score += len(intelligence["scam_keywords"]) * 10

    intelligence["risk_score"] = min(score, 100)

    return {
        "input_message": text,
        "extracted_intelligence": intelligence,
        "status": "analyzed"
    }


@app.get("/")
def root():
    return {"message": "Agentic Honey-Pot API is running"}
