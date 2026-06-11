from openai import OpenAI

from app.config.settings import settings


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.LLM_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

        self.model = settings.LLM_MODEL

    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=temperature
        )

        return response.choices[0].message.content