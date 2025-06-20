"""
IX-ZeroCool Gibson Adapter

Facilitates secure and fault-tolerant communication between IX-ZeroCool
and the IX-Gibson core intelligence node.
"""

import requests
import time
from config.gibson_config import GIBSON_API_URL, REQUEST_TIMEOUT_SECONDS, RETRY_ATTEMPTS, RETRY_BACKOFF_SECONDS

class GibsonAdapter:
    def __init__(self):
        self.endpoint = GIBSON_API_URL
        self.timeout = REQUEST_TIMEOUT_SECONDS
        self.retries = RETRY_ATTEMPTS
        self.backoff = RETRY_BACKOFF_SECONDS

    def query_gibson(self, question: str) -> dict:
        """
        Sends a structured query to IX-Gibson and returns the parsed result.

        Args:
            question (str): Input from user or module.

        Returns:
            dict: Parsed JSON response or fallback error payload.
        """
        payload = {
            "domain": "zerocool",
            "question": question,
            "from": "ix-zerocool"
        }
        for attempt in range(1, self.retries + 1):
            try:
                response = requests.post(self.endpoint, json=payload, timeout=self.timeout)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"[Gibson HTTP {response.status_code}] {response.text}")
            except requests.RequestException as e:
                print(f"[ZeroCool] Gibson request error (attempt {attempt}): {e}")

            if attempt < self.retries:
                time.sleep(self.backoff)

        return {"error": "Unable to retrieve response from IX-Gibson after multiple attempts."}
