# quantitative_circuit.py
class QuantitativeCircuit:
    def __init__(self, num_qubits=1):
        self.num_qubits = num_qubits
        self.gates = []

    def add_gate(self, gate, target_qubit, control_qubit=None):
        operation = {'gate': gate, 'target': target_qubit, 'control': control_qubit}
        self.gates.append(operation)

    def perform_operation(self):
        # Placeholder simulation: just print gates
        for op in self.gates:
            if op['control'] is not None:
                print(f"Apply {op['gate']} gate on qubit {op['target']} controlled by qubit {op['control']}")
            else:
                print(f"Apply {op['gate']} gate on qubit {op['target']}")

    def reset(self):
        self.gates = []

    def get_state(self):
        return f"Quantum circuit with {self.num_qubits} qubits and {len(self.gates)} gates."
 

    def apply_hadamard(self, qubit_index):
        print(f"Apply H gate on qubit {qubit_index}")

    def apply_cnot(self, control_qubit, target_qubit):
        print(f"Apply CNOT gate on qubit {target_qubit} controlled by qubit {control_qubit}")