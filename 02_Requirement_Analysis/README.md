# Phase 2: Requirement Analysis

## Project Title

**LegalEase – AI-Powered Legal Document Generator**

## Functional Requirements

The system should allow the user to:

1. Select the required legal document type.
2. Enter the details of the parties involved.
3. Enter important terms and conditions.
4. Enter the effective date.
5. Submit the information for document generation.
6. Generate a structured legal document using Google Gemini.
7. Preview the generated document.
8. Edit the generated document.
9. Download the generated document as a TXT file.

## Non-Functional Requirements

The application should:

- Provide a simple and user-friendly interface.
- Generate documents within a reasonable time.
- Provide clear and readable document output.
- Handle invalid or missing user inputs appropriately.
- Maintain secure handling of the Gemini API key.
- Provide reliable communication between the frontend and backend.

## Software Requirements

- Python
- Visual Studio Code
- Streamlit
- FastAPI
- Google Gemini API
- Pydantic
- Requests
- Python-dotenv
- Git and GitHub

## Hardware Requirements

- Laptop or desktop computer
- Minimum 4 GB RAM recommended
- Internet connection

## Input Requirements

The user provides:

- Document type
- Parties involved
- Terms and conditions
- Effective date

## Output Requirements

The system generates:

- A structured legal document draft
- Editable document preview
- TXT file for download

## AI Requirements

Google Gemini is used to generate the legal document based on the information provided by the user.

The AI-generated content should be treated as a draft and reviewed by a qualified legal professional before use.

## System Requirements

The system consists of:

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI Model:** Google Gemini
- **Communication:** HTTP API requests

## Expected Result

The completed system should allow users to enter basic legal document information and receive an AI-generated structured document that can be reviewed, edited, and downloaded.
