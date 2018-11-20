from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer
import Qconfig
from qiskit import Aer

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set the APIToken and API url

# set up quantum registers
num_individuals = 10
num_rows = 10

for x in range (0,num_individuals):
    for y in range (0, num_rows):
        qr = qp.create_quantum_register('qr', 3)

    




# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run, parallelize, and get results
results = qp.execute(["smiley_writer"], backend='ibmqx5', shots=1024)
stats = results.get_counts("smiley_writer")


 
