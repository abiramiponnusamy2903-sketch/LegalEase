from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import router


# =========================================================
# CREATE FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="LegalEase API",
    description="AI-powered legal document generation API",
    version="1.0.0"
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)


# =========================================================
# ROOT ENDPOINT
# =========================================================

@app.get("/")
def root():

    return {
        "message": "LegalEase API is running",
        "docs": "/docs",
        "health": "/health"
    }


# =========================================================
# INCLUDE API ROUTES
# =========================================================

app.include_router(router)