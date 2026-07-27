import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.asarray (x, dtype = float)
    y = np.asarray (y, dtype = float)

    if x.shape != y.shape:
        raise ValueError("length mismatch")

    return float (np.sum (x*y))
    pass