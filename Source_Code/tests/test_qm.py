# tests/test_qm.py
import unittest
from qm.quantum_mechanics import QuantumMechanics

class TestQuantumMechanics(unittest.TestCase):
    def setUp(self):
        self.qm = QuantumMechanics()
        self.qm.circuit.add_gate('H', target_qubit=0)
        self.qm.circuit.add_gate('CNOT', target_qubit=1, control_qubit=0)

    def test_perform_quantum_operation(self):
        result = self.qm.perform_quantum_operation()
        self.assertIsNotNone(result)
        self.assertTrue(hasattr(result, "summarize"))

    def test_analyze_quantum_state(self):
        state = self.qm.analyze_quantum_state()
        self.assertIsNotNone(state)
        self.assertTrue(hasattr(state, "analyze"))

if __name__ == "__main__":
    unittest.main()
