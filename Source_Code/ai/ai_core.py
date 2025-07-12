 
class AIComponent:
    def __init__(self, component_id, description):
        self.component_id = component_id
        self.description = description
        self.status = "initialized"

    def load_input_data(self, data_source):
        """Simulate loading input data from a source"""
        raise NotImplementedError("load_input_data must be implemented")

    def preprocess_data(self, raw_data):
        """Preprocessing steps before ML training"""
        raise NotImplementedError("preprocess_data must be implemented")

    def evaluate_signal(self, signal):
        """Evaluate incoming signal and decide next state"""
        raise NotImplementedError("evaluate_signal must be implemented")

    def archive_data(self):
        """Store processed data safely"""
        raise NotImplementedError("archive_data must be implemented")

    def __str__(self):
        return f"<AIComponent id={self.component_id}, status={self.status}>"
 