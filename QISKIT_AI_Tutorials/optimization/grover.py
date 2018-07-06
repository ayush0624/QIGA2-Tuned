# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

from qiskit_acqua.input import get_input_instance
from qiskit_acqua import run_algorithm

sat_cnf = """
c Example DIMACS 3-sat, with 3 solutions: 1 -2 3 0, -1 -2 -3 0, 1 2 -3 0
p cnf 3 5
-1 -2 -3 0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""

params = {
    'problem': {'name': 'search'},
    'algorithm': {'name': 'Grover'},
    'oracle': {'name': 'SAT', 'cnf': sat_cnf},
    'backend': {'name': 'local_qasm_simulator'}
}

result = run_algorithm(params)
print(result['result'])
