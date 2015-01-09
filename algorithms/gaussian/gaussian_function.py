# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
# https://en.wikipedia.org/wiki/Gaussian_function

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))

for mu, sig in [(-1,1),(0,2),(2,3)]:
    plt.plot(gaussian(np.linspace(-3, 3, 120), mu, sig))

plt.show()
