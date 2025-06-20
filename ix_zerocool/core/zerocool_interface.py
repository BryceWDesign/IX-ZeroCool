"""
IX-ZeroCool CLI Interface

Enables user access via command-line to route cybersecurity queries
through the ZeroCoolCore module and receive expert responses.
"""

from core.zerocool_core import ZeroCoolCore

def run_zerocool_cli():
    core = ZeroCoolCore()
    print("IX-ZeroCool — Cybersecurity & Digital Forensics Specialist")
    print("Ask your forensic or cyber inquiry below. Type 'exit' to quit.\n")

    while True:
        user_input = input("ZeroCool> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Shutting down IX-ZeroCool interface. Stay secure.")
            break
        output = core.process_query(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_zerocool_cli()
