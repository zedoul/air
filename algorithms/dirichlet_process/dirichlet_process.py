import numpy as np
from numpy.random import beta

def stick_breaking(alpha, k):
    betas = beta(1, alpha, k)
    remaining_pieces = np.append(1, np.cumprod(1 - betas[:-1]))
    p = betas * remaining_pieces
    return p/p.sum()

from numpy.random import choice

# p : probabilities given by stick_breaking or other group methods
# n : number of realization to create
def dirichlet_process(p, n, P0=np.random.randn):
    theta = P0(len(p))
    return np.random.choice(theta, size=n, p=p)

import matplotlib.pyplot as plt

p = stick_breaking(alpha=10, k=10)
dp = dirichlet_process(p, 1000)
_ = plt.hist(dp)
plt.show()
