from pydantic import BaseModel, Field


class DocumentRequest(BaseModel):
    document_type: str = Field(
        ...,
        description="Type of legal document to generate"
    )

    parties: str = Field(
        ...,
        description="Names and details of the parties"
    )

    terms: str = Field(
        ...,
        description="Important terms and conditions"
    )

    effective_date: str = Field(
        default="",
        description="Date on which the document becomes effective"
    )


class DocumentResponse(BaseModel):
    document_type: str
    content: str
    mode: str