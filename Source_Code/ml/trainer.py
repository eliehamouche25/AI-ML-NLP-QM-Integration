# ml/trainer.py

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

class SimpleTrainer:
    def __init__(self, model_name="DefaultModel"):
        self.model_name = model_name
        self.model = LogisticRegression()

    def train(self, X_train, y_train):
        print(f"Training model {self.model_name}...")
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Evaluation accuracy: {accuracy:.2f}")
        return accuracy

    def export_model(self, filename):
        joblib.dump(self.model, filename)
        print(f"Model saved as {filename}")