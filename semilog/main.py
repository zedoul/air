import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.01, 20.0, 0.01)
plt.semilogy(t, np.exp(-t/5.0))
plt.semilogy(t, np.exp(-t/1.0))
plt.semilogy(t, np.exp(t/1.0))
plt.title('semilogy')
plt.grid(True)
plt.show()
