from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, BasicAer, IBMQ
from qiskit.tools.visualization import circuit_drawer
from qiskit.tools.visualization import plot_histogram

# set up quantum registers
qubit_number = 2
register_number = 7
register_count = 0

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
print(IBMQ.backends(name='ibmq_qasm_simulator', operational=True))
print(IBMQ.backends())
realBackend = IBMQ.backends(name='ibmq_qasm_simulator', operational=True)[0]
print(realBackend)
#device = IBMQ.get_backend(realBackend)

register_count = 0
job_results = []
myMap = [[0, 1], [1, 2],
                 [0, 3], [1, 4], [2, 5],
                 [3, 4], [4, 5],
                 [3, 6]]

# run and parallelize
for qr in registers:
        cr = classicalregisters[register_count]
        qc = QuantumCircuit(qr, cr)
        job = execute(qc, realBackend, coupling_map=myMap)
        job.monitor()
        result = job.result()
        job_results.append(result.get_counts(qc))
        print(result) 
        register_count = register_count + 1

profit = []
stringVals = []
binaryString = ""
chromosomeCount = 0

for current_result in job_results:
        #get binary string
        DoubleZeroVal = current_result.get('00')
        stringVals.append(DoubleZeroVal)
        ZeroOneVal = current_result.get('01')
        stringVals.append(ZeroOneVal)
        OneZeroVal = current_result.get('10')
        stringVals.append(OneZeroVal)
        DoubleOneVal = current_result.get('11')
        stringVals.append(DoubleOneVal)
        stringVals.sort(reverse=True)
        highestVal = stringVals[0]

        if highestVal == DoubleOneVal:
                binaryString = binaryString + '11'
        elif highestVal == OneZeroVal:
                binaryString = binaryString + '10'
        elif highestVal == ZeroOneVal:
                binaryString = binaryString + '01'
        elif highestVal == DoubleZeroVal:
                binaryString = binaryString + '00'
        
        chromosomeCount = chromosomeCount + 1

        #evaluate knapsack 
        if chromosomeCount % 2 != 0:
                value = knapsack(binaryString)
                profit.append(value)

                binaryString = ""

profit.sort(reverse=True)
b = profit[0]
register_count = 0
j = 2
jString = "" 

for qr in registers:
        #determining probability amplitudes
        cr = classicalregisters[register_count]
        qc = QuantumCircuit(qr, cr)
        job_sim = execute(qc, simulator)
        sim_result = job_sim.result()
        probability_amplitude = sim_result.get_statevector()

        DoubleZeroRegister = probability_amplitude[0]
        ZeroOneRegister = probability_amplitude[1]
        OneZeroRegister = probability_amplitude[2]
        DoubleOneRegister = probability_amplitude[3]

        if register_count%2 == 0:
                jString = b[:j]
        else:
                jString = b[j:]

        if jString == '00':
                DoubleZeroRegister = 0.95(DoubleZeroRegister)
        elif jString == '01':
                ZeroOneRegister = 0.95(ZeroOneRegister)
        elif jString == '10':
                OneZeroRegister = 0.95(OneZeroRegister)
        elif jString == '11':
                DoubleOneRegister = 0.95(DoubleOneRegister)

        



        









        




