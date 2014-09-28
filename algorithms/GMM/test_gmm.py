import numpy as np
from sklearn import mixture

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.mlab as mlab

#n_samples = 3000
#np.random.seed(0)
#l = np.random.rand(n_samples,1)
#
#fig, ax = plt.subplots()
#
#ax.plot(range(0,n_samples),l)

mu, sigma = 0, 0.1 
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')


#mean = 0
#variance = 1
#sigma = np.sqrt(variance)
#x = np.linspace(-3,3,100)
#plt.plot(x,mlab.normpdf(x,mean,sigma))


plt.show()
