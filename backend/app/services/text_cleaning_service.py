from app.utils.text_utils import normalize_whitespace


class TextCleaningService:

    @staticmethod
    def clean(text: str):

        text = normalize_whitespace(text)

        return text