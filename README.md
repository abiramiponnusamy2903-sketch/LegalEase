# ⚖️ LegalEase

## AI-Powered Legal Document Generator

LegalEase is an AI-powered application that generates professional legal document drafts based on user-provided information.

### Features

- AI-assisted legal document generation
- Non-Disclosure Agreement
- Employment Contract
- Residential Lease Agreement
- Document preview and editing
- Download generated document as TXT
- FastAPI backend
- Streamlit frontend
- Google Gemini integration

## Technologies Used

- Python
- FastAPI
- Streamlit
- Google Gemini
- Pydantic
- Requests
- Uvicorn

## Project Structure

```text
LegalEase/
├── assets/
├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── schemas.py
│   ├── config.py
│   ├── ai_core/
│   │   └── gemini_generator.py
│   └── services/
├── frontend/
│   └── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
