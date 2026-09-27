from backend.config import settings


class GeminiDocumentGenerator:
    """
    Generates legal document drafts using Google Gemini.

    If no Gemini API key is configured, the application uses
    a demo document so that the project can still be tested.
    """

    def __init__(self):
        self.api_key = settings.gemini_api_key
        self.model_name = settings.gemini_model

    def list_available_models(self):
        """
        List Gemini models available to the configured API key.
        """

        from google import genai

        client = genai.Client(api_key=self.api_key)

        models = client.models.list()

        return [
            
            model.name
            for model in models
            if "generateContent" in getattr(model, "supported_actions", [])
        ]

    def generate_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str = ""
    ):
        """
        Generate a legal document.

        Returns:
            tuple[str, str]:
                Generated document text and generation mode.
        """

        if not self.api_key or self.api_key == "YOUR_GEMINI_API_KEY_HERE":
            return self._demo_document(
                document_type,
                parties,
                terms,
                effective_date
            )

        try:
            from google import genai

            client = genai.Client(api_key=self.api_key)

            prompt = self._build_prompt(
                document_type=document_type,
                parties=parties,
                terms=terms,
                effective_date=effective_date
            )

            response = client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )

            generated_text = response.text

            if not generated_text:
                raise ValueError("Gemini returned an empty response.")

            return generated_text.strip(), "gemini"

        except Exception as exc:
            print(f"Gemini generation error: {exc}")

            # Keep the application usable even if Gemini
            # is temporarily unavailable.
            return self._demo_document(
                document_type,
                parties,
                terms,
                effective_date
            )

    def _build_prompt(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str
    ) -> str:

        date_text = (
            effective_date.strip()
            if effective_date
            else "Not specified"
        )

        return f"""
You are a professional legal-document drafting assistant.

Create a clear and professionally structured draft for the following
legal document.

DOCUMENT TYPE:
{document_type}

PARTIES:
{parties}

IMPORTANT TERMS:
{terms}

EFFECTIVE DATE:
{date_text}

Requirements:

1. Create a professional legal document.
2. Use clear headings and sections.
3. Include the parties and their roles.
4. Include the important terms provided by the user.
5. Include the effective date where appropriate.
6. Use numbered sections when useful.
7. Do not invent unnecessary personal information.
8. Keep the language professional and understandable.
9. Include a short drafting disclaimer at the end stating that the
   document is an AI-generated draft and should be reviewed by a
   qualified legal professional.

Return only the document draft.
"""

    def _demo_document(
        self,
        document_type: str,
        parties: str,
        terms: str,
        effective_date: str
    ):
        """
        Creates a demo document when Gemini API access is not configured.
        """

        date_text = (
            effective_date.strip()
            if effective_date
            else "Not specified"
        )

        term_list = [
            term.strip()
            for term in terms.split(";")
            if term.strip()
        ]

        if not term_list:
            term_list = [
                "The parties agree to comply with the terms of this document."
            ]

        terms_text = "\n".join(
            f"{index}. {term}"
            for index, term in enumerate(term_list, start=1)
        )

        document = f"""
{document_type.upper()}

1. PARTIES

{parties}

2. EFFECTIVE DATE

This document shall become effective on {date_text}.

3. TERMS AND CONDITIONS

{terms_text}

4. GENERAL PROVISIONS

The parties agree to perform their respective obligations in
accordance with the terms and conditions described in this document.

Any amendment to this document should be made in writing and agreed
to by the relevant parties.

5. SIGNATURES

Party / Representative 1: ______________________________

Signature: _____________________________________________

Date: _________________________________________________


Party / Representative 2: ______________________________

Signature: _____________________________________________

Date: _________________________________________________


DISCLAIMER

This document is an AI-generated draft provided by LegalEase for
informational and drafting purposes only. It is not legal advice and
should be reviewed by a qualified legal professional before use.
""".strip()

        return document, "demo"
