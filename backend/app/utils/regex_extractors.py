#Generic Helper

import re


def find_first_match(text: str, patterns: list):

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match

    return None

#Loan Amount Extractor

def extract_loan_amount(text: str):

    patterns = [

        r"loan amount[:\s]*₹?\s*([\d,]+)",

        r"principal amount[:\s]*₹?\s*([\d,]+)",

        r"sanctioned amount[:\s]*₹?\s*([\d,]+)",

        r"amount financed[:\s]*₹?\s*([\d,]+)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return float(
            match.group(1).replace(",", "")
        )

    return None

# Interest Rate Extractor

def extract_interest_rate(text: str):

    patterns = [

        r"interest rate[:\s]*([\d.]+)\s*%",

        r"roi[:\s]*([\d.]+)\s*%",

        r"annual interest[:\s]*([\d.]+)\s*%"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return float(match.group(1))

    return None


# EMI Extractor

def extract_emi_amount(text: str):

    patterns = [

        r"emi[:\s]*₹?\s*([\d,]+)",

        r"monthly installment[:\s]*₹?\s*([\d,]+)",

        r"equated monthly installment[:\s]*₹?\s*([\d,]+)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return float(
            match.group(1).replace(",", "")
        )

    return None

# Duration Extractor

def extract_duration(text: str):

    patterns = [

        r"(\d+)\s*months",

        r"loan tenure[:\s]*(\d+)",

        r"repayment tenure[:\s]*(\d+)",

        r"duration[:\s]*(\d+)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return int(match.group(1))

    return None

# Processing Fee Extraction

def extract_processing_fee(text: str):

    patterns = [

        r"processing fee[:\s]*₹?\s*([\d,]+)",

        r"loan processing fee[:\s]*₹?\s*([\d,]+)",

        r"documentation charges[:\s]*₹?\s*([\d,]+)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return float(
            match.group(1).replace(",", "")
        )

    return None

# Foreclosure Charges

def extract_foreclosure_charges(text: str):

    patterns = [

        r"foreclosure charges[:\s]*(.*?)(?:\.|\n)",

        r"prepayment charges[:\s]*(.*?)(?:\.|\n)",

        r"loan closure charges[:\s]*(.*?)(?:\.|\n)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return match.group(1).strip()

    return None

# Late Payment Fee

def extract_late_payment_fee(text: str):

    patterns = [

        r"late payment fee[:\s]*(.*?)(?:\.|\n)",

        r"late payment charges[:\s]*(.*?)(?:\.|\n)",

        r"delay charges[:\s]*(.*?)(?:\.|\n)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return match.group(1).strip()

    return None

# Interest Type Detection

def detect_interest_type(text: str):

    floating_patterns = [

        r"floating rate",

        r"floating interest",

        r"variable interest",

        r"repo linked"
    ]

    fixed_patterns = [

        r"fixed rate",

        r"fixed interest"
    ]

    for pattern in floating_patterns:

        if re.search(
            pattern,
            text,
            re.IGNORECASE
        ):
            return "FLOATING"

    for pattern in fixed_patterns:

        if re.search(
            pattern,
            text,
            re.IGNORECASE
        ):
            return "FIXED"

    return "UNKNOWN"

# Penalty Detection

def extract_penalty_clause(text: str):

    patterns = [

        r"penalty[:\s]*(.*?)(?:\.|\n)",

        r"penal interest[:\s]*(.*?)(?:\.|\n)",

        r"default charges[:\s]*(.*?)(?:\.|\n)"
    ]

    match = find_first_match(
        text,
        patterns
    )

    if match:
        return match.group(1).strip()

    return None

