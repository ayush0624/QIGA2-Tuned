from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer
from qiskit import Aer


qr = QuantumRegister(3)

cr = ClassicalRegister(3)

circuit = QuantumCircuit(qr, cr)

circuit.x(qr[0])
circuit.x(qr[1])
circuit.ccx(qr[0], qr[1], qr[2])

circuit.cx(qr[0], qr[1])

circuit.measure(qr, cr)
circuit_drawer(circuit)

backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
job.status()
result = job.result()
result.get_counts(circuit)
 
