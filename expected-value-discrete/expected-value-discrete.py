import numpy as np

def expected_value_discrete(x, p):

    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)

    if len(x) != len(p):
        raise ValueError

    if not np.isclose(np.sum(p), 1):
        raise ValueError

    return float(np.sum(x * p))
    
    pass
