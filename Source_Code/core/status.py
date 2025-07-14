# core/status.py

class Status:
    def __init__(self, success=True, message="", error=None):
        """
        success: Boolean flag indicating if the operation succeeded.
        message: Descriptive message or log.
        error: Optional exception or error info.
        """
        self.success = success
        self.message = message
        self.error = error

    def __str__(self):
        return f"Status(success={self.success}, message='{self.message}', error={self.error})"