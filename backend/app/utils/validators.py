ALLOWED_EXTENSIONS = [".pdf"]

MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


def validate_pdf(filename: str):
    return filename.lower().endswith(".pdf")