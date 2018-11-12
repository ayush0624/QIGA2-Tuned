from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QuantumProgram
from qiskit import execute
from qiskit.tools.visualization import circuit_drawer
import Qconfig

qp = QuantumProgram()
qp.set_api(Qconfig.APItoken, Qconfig.config["url"]) # set the APIToken and API url

# set up registers and program
qr = qp.create_quantum_register('qr', 16)
cr = qp.create_classical_register('cr', 16)
qc = qp.create_circuit('simons algorithm', [qr], [cr])


def create_dict(simons_string):
    dict = {
        "00": simons_string,
        "01": simons_string + 1, 
        simons_string: "00", 
        simons_string + 1: "01"
    }

    return  dict


data = create_dict('10')

qc.h(qr)

def mygate():
    pass


mygate()

qc.h(qr)


qc.barrier(qr)

# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run and get results
results = qp.execute(["smiley_writer"], backend='ibmqx5', shots=1024)
stats = results.get_counts("smiley_writer")


 
