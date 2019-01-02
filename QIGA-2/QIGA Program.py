from qiskit import ClassicalRegister, QuantumProgram
from qiskit import QuantumRegister, QuantumCircuit, , execute
from qiskit.tools.visualization import circuit_drawer
import Qconfig
from qiskit.tools.visualization import plot_histogram




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
        print(cr)

#determining probability amplitudes        
simulator = Aer.backends(name='statevector_simulator')[0]
results = qp.execute(qc, simulator, shots=1024)
result = job.result()
result.get_statevector()

#Knapsack function

def knapsack():
    print("my function")


# run, parallelize, and get results
backend = Aer.get_backend('imbqx5')
results = qp.execute(qc, backend, shots=1024)
