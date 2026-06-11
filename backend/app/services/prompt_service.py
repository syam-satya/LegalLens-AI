from pathlib import Path


class PromptService:

    PROMPT_DIR = Path(
        "app/prompts"
    )

    @classmethod
    def load(
        cls,
        filename: str
    ) -> str:

        path = (
            cls.PROMPT_DIR /
            filename
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()