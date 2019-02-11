from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, BasicAer, IBMQ
from qiskit.tools.visualization import circuit_drawer
from qiskit.tools.visualization import plot_histogram
from qiskit.mapper import CouplingMap, Layout
import random

# set up quantum registers
qubit_number = 2
register_number = 4
weight_count = register_number/2
register_count = 0

# Choose a real device 
APItoken = '5b2f71479eae0159258df0ece626df4f137a6fa7126058500c086b17aa23333b244c003475c8b7f1c2c162c52fc81f2d272d300881e872cf1ba28a3060afe090'
url = 'https://quantumexperience.ng.bluemix.net/api'

#Choose Device
IBMQ.enable_account(APItoken, url=url)
IBMQ.load_accounts()
print(IBMQ.backends(name='ibmq_qasm_simulator', operational=True))
print(IBMQ.backends())
realBackend = IBMQ.backends(name='ibmq_qasm_simulator', operational=True)[0]
print(realBackend)

#Set up Probability Amplitude Simulator
simulator = BasicAer.backends(name='statevector_simulator')[0]

#Create quantum population and quantum chromosomes
registers = [QuantumRegister(qubit_number) for i in range(register_number)]
classicalregisters = [ClassicalRegister(qubit_number) for i in range(register_number)]
print(registers)
print(classicalregisters)

job_results = []
weightVals = []
profitVals = []
totalWeight = 0
w_o = 0
p_o = 0
cap = 0

for x in weight_count:
        w_o = int((random.random() * 9) + 1)
        p_o = w_i + 5

        weightVals.append(w_o)
        profitVals.append(p_o)

#superposition and measurement
for qr in registers:
        cr = classicalregisters[register_count]
        qc = QuantumCircuit(qr, cr)
        qc.h(qr)
        meas= QuantumCircuit(qr, cr)
        meas.measure(qr, cr)
        register_count = register_count + 1 
        
        realBackend = IBMQ.backends(name='ibmq_qasm_simulator')[0]
        circ = qc+meas
        result = execute(circ, realBackend, shots=1000).result()
        counts  = result.get_counts(circ)
        job_results.append(counts)
        print(counts)
        plot_histogram(counts)
        
print(job_results)

#Knapsack function
def knapsack(data, weight, p):
    profitVals.append(p)
    weightVals.append(weight)

    totalWeight = sum(weightVals)

    functionVal = p * data
    cap = 0.5 * totalWeight

    if(functionVal > cap):
        functionVal = 0

    return functionVal


register_count = 0
profit = []
stringVals = []
binaryString = ""
chromosomeCount = 0
weights = 0
p_i = 0
w_i = 0

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

        print(chromosomeCount)

        #evaluate knapsack 
        if chromosomeCount % 2 == 0:
                print(binaryString)
                p_i = weightVals[weights]
                w_i = profitVals[weights]

                binaryVal = int(binaryString,2)
                print("binary_val" + binaryVal)
                value = knapsack(binaryVal, w_i, p_i)
                profit.append(value)

                binaryString = ""
                weights = weights + 1


profit.sort(reverse=True)
print(profit)

b = profit[0]
register_count = 0
j = 2
jString = "" 

# for qr in registers:
#         #determining probability amplitudes
#         cr = classicalregisters[register_count]
#         qc = QuantumCircuit(qr, cr)
#         job_sim = execute(qc, simulator)
#         sim_result = job_sim.result()
#         probability_amplitude = sim_result.get_statevector()

#         DoubleZeroRegister = probability_amplitude[0]
#         ZeroOneRegister = probability_amplitude[1]
#         OneZeroRegister = probability_amplitude[2]
#         DoubleOneRegister = probability_amplitude[3]

#         if register_count%2 == 0:
#                 jString = b[:j]
#         else:
#                 jString = b[j:]

       

        



        









        




