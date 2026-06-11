from pathlib import Path

import pdfplumber


class PDFService:

    @staticmethod
    def extract_text(pdf_path: str) -> str:

        extracted_text = []

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text.append(page_text)

        return "\n".join(extracted_text)

    @staticmethod
    def save_uploaded_file(file, destination: str):

        with open(destination, "wb") as buffer:
            buffer.write(file.file.read())