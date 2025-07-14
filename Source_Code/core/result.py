# core/result.py

class Result:
    def __init__(self, content=None, metadata=None):
        """
        content: Main result content (can be dict, str, list, etc.)
        metadata: Optional dictionary with additional information (e.g., timestamps, source, runtime)
        """
        self.content = content if content is not None else {}
        self.metadata = metadata if metadata is not None else {}

    def __str__(self):
        return f"Result(content={self.content}, metadata={self.metadata})"