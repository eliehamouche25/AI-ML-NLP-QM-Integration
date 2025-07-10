 # main
from ai.sensor_ai import SensorAI
from ml.trainer import SimpleTrainer
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from nlp.nlp_core import SimpleNLPProcessor

def main():
    print("🧠 Initializing AI Component...")
    ai = SensorAI(component_id="AI001", description="Basic Sensor AI")
    
    # Simulate data loading & preprocessing
    ai.load_input_data("iris_dataset")
    raw_data = "IRIS DATA SAMPLE"
    processed_data = ai.preprocess_data(raw_data)
    print("Processed data:", processed_data)

    # Simulate signal to transition to ML
    signal_result = ai.evaluate_signal("Start ML")
    if signal_result == "TransitionToML":
        ai.archive_data()
        
        print("\n📊 Starting ML Training Phase...")
        trainer = SimpleTrainer(model_name="IrisClassifier")

        # Load and split real data
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42
        )

        # Train and evaluate
        trainer.train(X_train, y_train)
        acc = trainer.evaluate(X_test, y_test)
        trainer.export_model("iris_model.pkl")

        print(f"🎉 ML Pipeline Complete! Final accuracy: {acc:.2f}")

    else:
        print("Signal does not trigger ML phase.")


    # NLP Processing
    print("\n🧠 Starting NLP Processing...")

    nlp = SimpleNLPProcessor()
    sample_text = "I really enjoy working on this AI–ML–NLP–QM integration project."
    nlp.set_text(sample_text)
    tokens = nlp.tokenize()
    parsed = nlp.parse(tokens)
    sentiment = nlp.recognize_intent()
    response = nlp.generate_text()
    print(f"📨 Final NLP Output: {response}")
 
if __name__ == "__main__":
    main()
