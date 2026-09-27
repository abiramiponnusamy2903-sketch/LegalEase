from fastapi import APIRouter, HTTPException

from backend.schemas import DocumentRequest, DocumentResponse
from backend.ai_core.gemini_generator import GeminiDocumentGenerator


router = APIRouter()

generator = GeminiDocumentGenerator()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "LegalEase API"
    }


@router.get("/models")
def list_models():
    try:
        return {
            "models": generator.list_available_models()
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Model listing failed: {str(exc)}"
        )


@router.post(
    "/generate",
    response_model=DocumentResponse
)
def generate_document(request: DocumentRequest):
    try:
        content, mode = generator.generate_document(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date
        )

        return DocumentResponse(
            document_type=request.document_type,
            content=content,
            mode=mode
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Document generation failed: {str(exc)}"
        )