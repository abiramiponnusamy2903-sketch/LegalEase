import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self):
        self.gemini_api_key = os.getenv(
            "GEMINI_API_KEY",
            ""
        )

        self.gemini_model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

        self.backend_url = os.getenv(
            "BACKEND_URL",
            "http://127.0.0.1:8000"
        )

        self.logo_path = os.getenv(
            "LOGO_PATH",
            "assets/logo.png"
        )


settings = Settings()