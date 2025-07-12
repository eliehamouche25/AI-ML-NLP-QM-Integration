# qm/quantum_mechanics.py
from qm.quantitative_circuit import QuantitativeCircuit
from qm.qresult import QResult
from qm.qstate import QState

class QuantumMechanics:
    def __init__(self):
        self.circuit = QuantitativeCircuit()
        self.qresult = QResult()
        self.qstate = QState(state_data=str(self.circuit))

    def perform_quantum_operation(self):
        return self.qresult

    def analyze_quantum_state(self):
        return self.qstate
    