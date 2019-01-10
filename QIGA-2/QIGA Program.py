from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, BasicAer, IBMQ
from qiskit.tools.visualization import circuit_drawer
from qiskit.tools.visualization import plot_histogram

# set up quantum registers
qubit_number = 2
register_number = 10

#Create quantum population and quantum chromosomes
registers = [QuantumRegister(qubit_number) for i in range(register_number)]
classicalregisters = [ClassicalRegister(qubit_number) for i in range(register_number)]
qc = QuantumCircuit(*registers)

#superposition and measurement
for qr in registers:
    for cr in classicalregisters:
        qc.h(qr)
        qc.measure(qr, cr)
        print(cr)

#determining probability amplitudes        
simulator = BasicAer.backends(name='statevector_simulator')[0]
results = execute(qc, simulator, shots=1024)
result = job.result()
result.get_statevector()

#Knapsack function

def knapsack():
    print("my function")

# Choose a real device to simulate
APItoken = '5b2f71479eae0159258df0ece626df4f137a6fa7126058500c086b17aa23333b244c003475c8b7f1c2c162c52fc81f2d272d300881e872cf1ba28a3060afe090'
url = 'https://quantumexperience.ng.bluemix.net/api'

IBMQ.save_account(APItoken, url=url)
IBMQ.load_accounts()
realBackend = IBMQ.backends(name='ibmqx2')[0]
device = IBMQ.get_backend(realBackend)
config = device.config;

# run, parallelize, and get results
job_sim = execute(qc, realBackend, config=config)
sim_result = job_sim.result()

print(sim_result.get_counts(qc))

