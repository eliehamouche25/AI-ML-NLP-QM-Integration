
from nlp.entities import Entity

class Analysis:
    def __init__(self):
        pass  # Future config/params could go here

    def extract_entities(self, text: str):
        """
        Simulated named entity recognition (NER).
        For now, we use simple keyword-based extraction.
        """
        entities = []

        if "OpenAI" in text:
            entities.append(Entity("OpenAI", "ORG", text.index("OpenAI"), text.index("OpenAI") + len("OpenAI")))
        if "Elie" in text:
            entities.append(Entity("Elie", "PERSON", text.index("Elie"), text.index("Elie") + len("Elie")))

        return entities
    
 