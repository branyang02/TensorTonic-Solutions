import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    arr = np.asarray(x, dtype="float")
    arr = 1 / (1 + np.exp(-arr))
    return arr