from qiskit.tools.visualization import plot_histogram
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer


qr = QuantumRegister(2)
cr = ClassicalRegister(2)

# quantum circuit to make a Bell state
qc = QuantumCircuit(qr,cr)
qc.h(qr)


meas = QuantumCircuit(qr,cr)
meas.measure(qr, cr)

# execute the quantum circuit
backend = BasicAer.get_backend('qasm_simulator') # the device to run on
circ = qc+meas
result = execute(circ, backend, shots=1000).result()
counts  = result.get_counts(circ)
print(counts)
plot_histogram(counts)

