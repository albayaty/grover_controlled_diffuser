# Grover controlled-diffuser (*CU<sub>s<sub>*)

[![Tests](https://github.com/albayaty/grover_controlled_diffuser/actions/workflows/tests.yml/badge.svg)](https://github.com/albayaty/grover_controlled_diffuser/actions/workflows/tests.yml)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebook-blue.svg)](https://jupyter.org)
[![Python](https://img.shields.io/badge/Python-%E2%89%A5%203.9-blue.svg)](https://www.python.org)
[![Qiskit](https://img.shields.io/badge/Qiskit-%E2%89%A5%201.0-blue.svg)](https://www.ibm.com/quantum/qiskit)
[![Ecosystem](https://img.shields.io/badge/Qiskit-ecosystem-blue.svg)](https://www.ibm.com/quantum/ecosystem)
![Platforms](https://img.shields.io/badge/Platforms-Linux%20%7C%20macOS%20%7C%20Windows-blue)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue)](https://www.apache.org/licenses/LICENSE-2.0)

The Grover controlled-diffuser (*CU<sub>s<sub>*) is a quantum diffusion operator for Grover’s algorithm that searches for all solutions for Boolean oracles only, since the standard Grover diffuser (*U<sub>s<sub>*) fails to find correct solutions for Boolean oracles in some logical structures! The *CU<sub>s<sub>* operator relies on the states of the output qubit (as the reflection of Boolean decisions from a Boolean oracle), without relying on the phase kickback as illustrated below.

![Grover-algorithm](images/Grover-algorithm.png "Grover's algorithm with the CUs operator")

Thereby, the *CU<sub>s<sub>* operator successfully searches for all solutions for Boolean oracles regardless of their logical structures, e.g., POS, SOP, DSOP, ESOP, ANF (Reed-Muller), XOR SAT (CNF-XOR SAT and DNF-XOR SAT), just to name a few.

Therefore, the *CU<sub>s<sub>* operator can replace the standard *U<sub>s<sub>* operator for Grover’s algorithm of Boolean oracles representing practical applications in the topics of digital synthesizers, robotics, computer vision, machine learning, etc., in the quantum domain.

For more information, please read our paper entitled **"A concept of controlling Grover diffusion operator: A new approach to solve arbitrary Boolean-based problems"**, available at https://doi.org/10.1038/s41598-024-74587-y

## Installation

Install the latest version of *CU<sub>s<sub>* operator using the `pip` command:

```bash
pip install git+https://github.com/albayaty/grover_controlled_diffuser@main
```

Instead, the *CU<sub>s<sub>* operator can be manually installed as stated in the following steps:

1. Download this repository to your computer, as a ZIP file.
2. Extract this file to a folder, e.g., `grover_controlled_diffuser`.
3. Use the `terminal` (or the `Command Prompt`) to `cd` to the `grover_controlled_diffuser` folder.
4. Install the `setup.py` file using the following command:

   ```bash
    python setup.py install
    ```
    Or, using this command:

    ```bash
    python3 -m pip install .
    ```

## Usage

First of all, please be sure that the following prerequisite packages have been installed:

- [X] `qiskit` (version >= 1.0).
- [X] `qiskit_aer` (simulating quantum circuits locally).
- [X] `qiskit_ibm_runtime` (transpiling and executing quantum circuits on IBM quantum computers).
- [X] `qiskit.visualization` (plotting histograms, distributions, etc.).
- [X] `matplotlib` (drawing quantum circuits).

Next, the callable function of the *CU<sub>s<sub>* operator is expressed as follows.

```python
CUs(quantum_circuit, inputs, output, barriers=False)
```

Where,

`quantum_circuit`: the quantum circuit of Grover's algorithm,

`inputs`: the list of input qubits' indices of a Boolean oracle,

`output`: the index of output qubit of a Boolean oracle, and

`barriers`: draw barriers (separators) around the *CU<sub>s<sub>* operator, its default value is `False`.
    
Finally, the `CUs` function returns the quantum circuit of Grover's algorithm with the constructed *CU<sub>s<sub>* operator. Note that this function does not add the measurement gates.

## Examples

Initially, import the required Python and Qiskit libraries (including our `grover_controlled_diffuser`):
```python
from qiskit import *
from qiskit_aer import AerSimulator
from qiskit.visualization import *
from grover_controlled_diffuser import *
import matplotlib.pyplot as plt
%matplotlib inline
```

Then, let's construct and use the *CU<sub>s<sub>* operator in different scenarios as follows.

1. The *CU<sub>s<sub>* operator (2 inputs and 1 output) surrounded by barriers:
    ```python
    inputs = [0,1]
    output = 2
    IN  = QuantumRegister( len(inputs), name = 'input'  )
    OUT = QuantumRegister( 1, name = 'output' )
    qc = QuantumCircuit(IN, OUT)
    qc = CUs(qc, inputs, output, barriers=True)     # Grover controlled-diffuser (CUs)
    qc.draw(output='mpl', style='bw', scale=1.0, fold=-1);
    ```    
    ![figure1](images/figure1.png)

2. Construct Grover's algorithm to solve a 4-bit Toffoli gate (as a Boolean oracle) using the *CU<sub>s<sub>* operator, in one Grover iteration (loop), and then measure the outcomes as the highest probabilities as solutions:
    ```python
    inputs = [0,1,2]
    output = 3
    IN  = QuantumRegister( len(inputs), name = 'input'  )
    OUT = QuantumRegister( 1, name = 'output' )
    MEAS = ClassicalRegister( len(inputs), name = 'clbits' )
    qc = QuantumCircuit(IN, OUT, MEAS)
    qc.h(inputs)
    qc.mcx(inputs, output)   # The Boolean oracle
    qc = CUs(qc, inputs, output, barriers=True)     # Grover controlled-diffuser (CUs)
    qc.measure(inputs, list(range(len(inputs))))
    qc.draw(output='mpl', style='bw', scale=1.0, fold=-1);
    simulator = AerSimulator()
    results = simulator.run(qc).result()
    counts  = results.get_counts(0)
    plot_distribution(counts, bar_labels=True, title="One solution is found when all inputs are in the |1> states");
    ```
    ![figure2a](images/figure2a.png)
    ![figure2b](images/figure2b.png)

3. Construct Grover's algorithm to solve an arbitrary Boolean oracle in POS structure, as (*a* + *b* + ¬*c*)(¬*a* + *c*)(¬*b* + *c*), using the *CU<sub>s<sub>* operator, in one Grover iteration (loop), and then measure the outcomes as the highest probabilities as solutions. **Note that such a Boolean oracle in POS structure is not solvable using the standard Grover diffuser (*U<sub>s<sub>*)!**
    ```python
    inputs = [0,1,2]
    ancillae = [3,4,5]
    output = 6
    IN  = QuantumRegister( len(inputs), name = 'input'  )
    ANC = QuantumRegister( len(ancillae), name = 'anc' )
    OUT = QuantumRegister( 1, name = 'output' )
    MEAS = ClassicalRegister( len(inputs), name = 'clbits' )
    qc = QuantumCircuit(IN, ANC, OUT, MEAS)
    qc.h(inputs)
    qc.barrier()
    # The Boolean oracle in POS structure:
    qc.x([0,1,3])
    qc.mcx([0,1,2],3)
    qc.x([0,1])
    qc.x([2,4])
    qc.ccx(0,2,4)
    qc.x(5)
    qc.ccx(1,2,5)
    qc.mcx([3,4,5],6)
    # The mirror (uncomputing):
    qc.ccx(1,2,5)
    qc.x(5)
    qc.ccx(0,2,4)
    qc.x([2,4])
    qc.x([0,1])
    qc.mcx([0,1,2],3)
    qc.x([0,1,3])
    qc = CUs(qc, inputs, output, barriers=True)     # Grover controlled-diffuser (CUs)
    qc.measure(inputs, list(range(len(inputs))))
    qc.draw(output='mpl', style='bw', scale=1.0, fold=-1);
    simulator = AerSimulator()
    results = simulator.run(qc).result()
    counts  = results.get_counts(0)
    plot_distribution(counts, bar_labels=True, title="Solutions");
    ```
    ![figure3a](images/figure3a.png)
    ![figure3b](images/figure3b.png)

## Reference

In case you are utilizing our Grover controlled-diffuser (*CU<sub>s<sub>*) in your research work, we would be grateful if you cited our publication:

A. Al-Bayaty and M. Perkowski, "A concept of controlling Grover diffusion operator: A new approach to solve arbitrary Boolean-based problems," *Scientific Reports*, vol. 14, pp. 1-16, 2024. [Online]. Available: https://doi.org/10.1038/s41598-024-74587-y

Or, using BibTeX style:

```bibtex
@article{grovercontrolleddiffuser,
    title={A concept of controlling Grover diffusion operator: a new approach to solve arbitrary Boolean-based problems},
    author={Ali Al-Bayaty and Marek Perkowski},
    journal={Scientific Reports},
    volume={14},
    pages={1-16},
    year={2024},
    publisher={Nature Publishing Group},
    url={https://doi.org/10.1038/s41598-024-74587-y}
}
```
