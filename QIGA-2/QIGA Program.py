from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, BasicAer, IBMQ
from qiskit.tools.visualization import circuit_drawer
from qiskit.tools.visualization import plot_histogram

# set up quantum registers
qubit_number = 2
register_number = 3
register_count = 0;

#Create quantum population and quantum chromosomes
registers = [QuantumRegister(qubit_number) for i in range(register_number)]
classicalregisters = [ClassicalRegister(qubit_number) for i in range(register_number)]


#Set up Probability Amplitude Simulator
simulator = BasicAer.backends(name='statevector_simulator')[0]

#superposition and measurement
for qr in registers:
        cr = classicalregisters[register_count]
        qc = QuantumCircuit(qr, cr)
        qc.h(qr)
        qc.measure(qr, cr)
        register_count = register_count + 1    

#Knapsack function

def knapsack(data):
    print("my function")

# Choose a real device 
APItoken = '5b2f71479eae0159258df0ece626df4f137a6fa7126058500c086b17aa23333b244c003475c8b7f1c2c162c52fc81f2d272d300881e872cf1ba28a3060afe090'
url = 'https://quantumexperience.ng.bluemix.net/api'

IBMQ.enable_account(APItoken, url=url)
IBMQ.load_accounts()
print(IBMQ.backends(name='ibmq_16_melbourne', operational=True))
print(IBMQ.backends())
realBackend = IBMQ.backends(name='ibmq_16_melbourne')[0]
print(realBackend)
#device = IBMQ.get_backend(realBackend)

# run and parallelize
job = execute(qc, realBackend, shots=1024, max_credits=10)
result = job.result()
print(result)

register_count = 0
profit = []

#evaluate knapsack function
for qr in registers:
        data = result.get_counts()[register_count] 
        value = knapsack(data)
        profit.append(value)
        register_count = register_count + 1

profit.sort(reverse=True)
b = profit[0]
register_count = 0

#determining probability amplitudes
for qr in registers:
        cr = classicalregisters[register_count]
        qc = QuantumCircuit(qr, cr)
        job_sim = execute(qc, simulator, shots=1024)
        sim_result = job_sim.result()
        sim_result.get_statevector()
        
            


