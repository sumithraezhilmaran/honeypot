
# Agentic Honey-Pot — Scam Intelligence Extraction API

## Features
- Accepts scam / suspicious messages
- Extracts:
  - Emails
  - Phone Numbers
  - URLs
  - Scam Keywords
- Generates Risk Score (0–100)
- API Key Authentication

## Installation

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn main:app --reload
```

## Endpoint

POST `/analyze`

Headers:
```
x-api-key: demo_api_key_123
```

Body:
```json
{
  "message": "You won a lottery! Click http://scam.com and send OTP"
}
```

## Output
Returns extracted intelligence + risk score.

---
Ready for hackathon submission ✅
