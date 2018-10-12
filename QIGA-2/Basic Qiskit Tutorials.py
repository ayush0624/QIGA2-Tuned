from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer


qr = QuantumRegister(3)

cr = ClassicalRegister(3)

circuit = QuantumCircuit(qr, cr)

circuit.measure(qr, cr)
circuit_drawer(circuit)

 
