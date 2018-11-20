from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer
import Qconfig
from qiskit import Aer

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set the APIToken and API url

# set up quantum registers

qr = qp.create_quantum_register('qr', 3)
cr = qp.create_classical_register('cr', 16)
qc = qp.create_circuit('simons algorithm', [qr], [cr])



# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run, parallelize, and get results
results = qp.execute(["smiley_writer"], backend='ibmqx5', shots=1024)
stats = results.get_counts("smiley_writer")


 
