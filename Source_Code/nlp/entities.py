# nlp/entities.py

class Entity:
    def __init__(self, text: str, entity_type: str, start: int, end: int):
        """
        :param text: The actual word/phrase extracted.
        :param entity_type: Type of entity, e.g., 'PERSON', 'ORG'.
        :param start: Starting index in the text.
        :param end: Ending index in the text.
        """
        self.text = text
        self.entity_type = entity_type
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Entity(text='{self.text}', type='{self.entity_type}', start={self.start},  end={self.end})"

