from google import genai

from app.core.config import settings


class LLMService:

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    @classmethod
    def generate(
        cls,
        prompt: str
    ):

        response = cls.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt
        )

        return response.text