import re


def extract_borrower_name(text: str):

    patterns = [
        r"borrower[:\s]+([A-Za-z ]+)",
        r"customer[:\s]+([A-Za-z ]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    return None


def extract_lender_name(text: str):

    patterns = [
        r"lender[:\s]+([A-Za-z ]+)",
        r"bank[:\s]+([A-Za-z ]+)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(1).strip()

    return None