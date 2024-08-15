# ----------------------------------------------------------------------
# Grover controlled-diffuser (CUs):
# ----------------------------------------------------------------------

def CUs(quantum_circuit, inputs, output, barriers=False):
    """
    This function constructs Grover controlled-diffuser (CUs), which is the 
    standard Grover diffuser (Us) of Grover's algorithm that is controlled 
    by the output qubit of a Boolean oracle. The CUs operator is well-designed
    to search for all solutions for Boolean oracles only, where the standard 
    Us operator fails to search for all solutions!
    
    Parameters
    ----------
    quantum_circuit: the quantum circuit of Grover's algorithm,
    inputs: the list of input qubits' indices of a Boolean oracle,
    output: the index of output qubit of a Boolean oracle, and
    barriers: draw barriers (separators) around the CUs operator, its default value is False.
    
    Returns
    -------
    The quantum circuit of Grover's algorithm with the Grover controlled-diffuser (CUs).
    
    For more information, please read our paper available at
    https://doi.org/10.21203/rs.3.rs-2997276/v1
    """
    
    if barriers:
	    quantum_circuit.barrier()
    
    # The 2nd rotation:
    quantum_circuit.h( inputs )
    
    # The conditional phase shift:
    quantum_circuit.x( inputs )
    quantum_circuit.x( output )
    
    # The phase inversion (CZ0):
    quantum_circuit.h( output )
    quantum_circuit.mcx( inputs, output )
    quantum_circuit.h( output )
    
    # The mirror (uncomputing):
    quantum_circuit.x( output )
    quantum_circuit.x( inputs )    
    quantum_circuit.h( inputs )
    
    if barriers:
	    quantum_circuit.barrier()
    
    return quantum_circuit


# ----------------------------------------------------------------------
# Counting the number of gates of the CUs operator:
# ----------------------------------------------------------------------

def num_CUs_gates(qubits):
    """
    This function counts the number of gates of Grover controlled-diffuser (CUs).
    
    Parameters
    ----------
    qubits: the number of qubits (n-1 inputs and 1 output), where qubits >= 3.
    
    Returns
    -------
    The number of gates of Grover controlled-diffuser (CUs).
    """
    
    # Consistency checking:    
    if (qubits < 3):
	    print(f"\n⟩⟩⟩ ERROR: The CUs operator should have more than '{qubits}' qubits!")
	    print(f"⟩⟩⟩  INFO: The CUs operator has n qubits (n-1 inputs + 1 output), where n >= 3.\n")
	    return
    
    H = qubits*2
    X = qubits*2
    MCX = 1    
    gates = H + X + MCX
    
    return gates
