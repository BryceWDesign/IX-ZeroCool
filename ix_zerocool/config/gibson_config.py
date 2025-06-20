"""
Gibson Configuration — IX-ZeroCool

Defines endpoint, timeout, and retry strategy for communicating with IX-Gibson.
"""

# Base URL to reach the IX-Gibson central intelligence node
GIBSON_API_URL = "http://localhost:9000/api/query"

# Timeout duration for requests to Gibson (in seconds)
REQUEST_TIMEOUT_SECONDS = 5

# Number of retry attempts on failed connection
RETRY_ATTEMPTS = 3

# Seconds to wait between retries
RETRY_BACKOFF_SECONDS = 2
