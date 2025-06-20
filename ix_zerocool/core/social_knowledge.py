"""
IX-ZeroCool Core Social Engineering Knowledge Module

Provides foundational knowledge about social engineering tactics,
manipulation techniques, and human factors in cybersecurity.
"""

class SocialEngineeringKnowledge:
    def __init__(self):
        self.facts = {
            "phishing": "A fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity.",
            "pretexting": "Creating a fabricated scenario to steal someone's personal information.",
            "baiting": "Offering something enticing to lure victims into a trap.",
            "tailgating": "Gaining physical access to a restricted area by following authorized personnel.",
            "spear phishing": "A targeted phishing attack directed at specific individuals or organizations."
        }

    def get_fact(self, term: str) -> str:
        t = term.lower().strip()
        return self.facts.get(t, f"Unknown social engineering concept: '{term}' not found in ZeroCool’s knowledge base.")

# Standalone test
if __name__ == "__main__":
    sk = SocialEngineeringKnowledge()
    print(sk.get_fact("phishing"))
    print(sk.get_fact("baiting"))
    print(sk.get_fact("unknown tactic"))
