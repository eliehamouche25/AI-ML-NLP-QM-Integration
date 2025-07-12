# ml_model.py

class MLModel:
    def __init__(self, model_name: str, model_type: str):
        self.model_name = model_name
        self.model_type = model_type
        self.trained = False

    def train(self, training_data):
        print(f"Training {self.model_type} model: {self.model_name}")
        # Simulate training process
        self.trained = True

    def predict(self, input_data):
        if not self.trained:
            raise Exception("Model must be trained before prediction.")
        print(f"Predicting with model {self.model_name}")
        # Simulate prediction result
        return "predicted_output"
    
 