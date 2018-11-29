from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer
import Qconfig
from qiskit import Aer

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set the APIToken and API url

# set up quantum registers
qubit_number = 2
register_number = 10

registers = [qiskit.QuantumRegister(qubit_number) for i in range(register_number)]
classicalregisters = [qiskit.ClassicalRegister(qubit_number) for i in range(register_number)]
qc = qiskit.QuantumCircuit(*registers)


#superposition and measurement
for qr in registers:
    for cr in classicalregisters:
        qc.h(qr)
        qc.measure(qr, cr)



#Knapsack function

def knapsack():
    print("my function")


# run, parallelize, and get results
results = qp.execute(["smiley_writer"], backend='ibmqx5', shots=1024)
stats = results.get_counts("smiley_writer")


 
