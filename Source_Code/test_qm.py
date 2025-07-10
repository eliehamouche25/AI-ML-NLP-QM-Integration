# test_qm.py
from quantum_mechanics import QuantumMechanics

def test_qm_module():
    qm = QuantumMechanics()
    qm.circuit.add_gate('H', target_qubit=0)
    qm.circuit.add_gate('CNOT', target_qubit=1, control_qubit=0)

    result = qm.perform_quantum_operation()
    print(result.get_summary())

    state = qm.analyze_quantum_state()
    print(state.analyze())

if __name__ == "__main__":
    test_qm_module()