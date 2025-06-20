"""
IX-ZeroCool Utilities Module

Helper functions to normalize, sanitize, and validate social engineering queries
before forwarding to the query processor.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize input by trimming, collapsing whitespace,
    and removing unwanted characters.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\.\@\:\']+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Basic validation to check query length and character composition.
    """
    return bool(query and len(query) > 3 and any(c.isalnum() for c in query))

# Example usage
if __name__ == "__main__":
    test_cases = [
        "Define baiting",
        "   What is phishing?? ",
        "Explain tailgating!!",
        "Huh?"
    ]
    for test in test_cases:
        cleaned = clean_query(test)
        valid = is_valid_query(cleaned)
        print(f"Original: {test} → Cleaned: '{cleaned}' | Valid: {valid}")
