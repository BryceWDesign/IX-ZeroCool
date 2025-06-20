"""
IX-ZeroCool Core Logic

Handles interpretation and response logic specific to IX-ZeroCool's function
as a digital forensics and cybersecurity specialist, routed through IX-Gibson.
"""

from .gibson_adapter import GibsonAdapter

class ZeroCoolCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def process_query(self, question: str) -> str:
        """
        Processes a user query using Gibson, formatted for cybersecurity tasks.

        Args:
            question (str): Natural language query.

        Returns:
            str: Answer or error string.
        """
        response = self.gibson.query_gibson(question)
        if "error" in response:
            return f"[ZeroCool Error] {response['error']}"
        return response.get("answer", "[ZeroCool] No definitive answer returned.")
