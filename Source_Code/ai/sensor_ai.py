class SensorAI:
    def __init__(self, component_id, description=""):
        self.component_id = component_id
        self.description = description

    def load_input_data(self, source):
        print(f"Loading data from {source}...")

    def preprocess_data(self, data):
        print("Preprocessing data...")
        return data.lower()

    def evaluate_signal(self, signal):
        print(f"Evaluating signal: {signal}")
        return "TransitionToML" if signal == "Start ML" else "StayInAI"

    def archive_data(self):
        print("Archiving processed data...")
