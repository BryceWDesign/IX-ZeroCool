"""
IX-ZeroCool CLI Entry Point

Enables command-line interaction for social engineering and cybersecurity awareness queries.
"""

import sys
from core.query_processor import IXZeroCoolQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your social engineering question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXZeroCoolQueryProcessor()
    response = processor.process_query(query)

    print("\n🧠 IX-ZeroCool Response 🧠")
    print(response)

if __name__ == "__main__":
    main()
