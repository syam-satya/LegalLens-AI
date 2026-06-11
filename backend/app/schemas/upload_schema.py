from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    file_size: int
    extracted_characters: int
    status: str