import numpy as np
from numpy.random import beta

# alpha = proportion. \infty is uniform
# k = number of realization
def stick_breaking(alpha, k):
    betas = beta(1, alpha, k)
    remaining_pieces = np.append(1, np.cumprod(1 - betas[:-1]))
    p = betas * remaining_pieces
    return p/p.sum()

p = stick_breaking(alpha=1, k=10)
print p
