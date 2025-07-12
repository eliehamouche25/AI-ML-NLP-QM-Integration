 

from ml.ml_model import MLModel

class MLModule:
    def __init__(self, module_name):
        # Composition: the module creates and owns the model
        self.model = MLModel(model_name=f"{module_name}_model", model_type="Supervised")

    def train(self, training_data=None):
        self.model.train(training_data)
        return self.model.trained

    def predict(self, input_data):
        return self.model.predict(input_data)