"""
IX-ZeroCool Domain-Specific Query Processor

Processes social engineering and human factor queries,
returning clear explanations and advice based on core knowledge.
"""

from core.social_knowledge import SocialEngineeringKnowledge

class IXZeroCoolQueryProcessor:
    def __init__(self):
        self.knowledge = SocialEngineeringKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-ZeroCool, your social engineering AI. Ask me about phishing, pretexting, baiting, and related tactics. "
                "Examples: 'Define phishing', 'What is spear phishing?', 'Explain tailgating'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXZeroCoolQueryProcessor()
    print(qp.process_query("Define phishing"))
    print(qp.process_query("Explain baiting"))
    print(qp.process_query("What is tailgating?"))
