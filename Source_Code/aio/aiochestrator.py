from ml.ml_module import MLModule
from nlp.nlp_module import NLPModule
from qm.quantum_mechanics import QuantumMechanics
from core.result import Result
from core.status import Status

class AIOrchestrator:
      def __init__(self, name="AI_Center"):
        self.name = name
        self.ml_module = MLModule("ML_Main")
        self.nlp_module = NLPModule("NLP_Main")
        self.qm_module = QuantumMechanics("QM_Main")  
    
      def run_full_pipeline(self, text: str):
        sentiment = self.nlp_module.analyze_text(text)
        entities = self.nlp_module.process_text(text)
        ml_prediction = self.ml_module.train_and_predict(text)
        quantum_result = self.qm_module.perform_quantum_operation()

        result_content = {
            "sentiment": sentiment,
            "entities": [str(e) for e in entities],
            "ml_prediction": ml_prediction,
            "quantum_result": str(quantum_result),
        }

        return Result(result_content), Status(success=True)
