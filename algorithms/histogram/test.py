import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

n_samples = 100000
np.random.seed(0)
l = np.random.normal(-1,1**2,n_samples)

hist, bin_edges = np.histogram(l, bins=10, density=True)

fig, ax = plt.subplots()
ax.plot(bin_edges[0:10], hist)

plt.show()
