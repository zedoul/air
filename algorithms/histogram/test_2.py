import numpy as np

np.random.seed(1)

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html
n_samples = 100000
np.random.seed(0)
l1 = np.random.normal(-1,1**2,n_samples)
print type(l1)
l2 = np.random.normal(2,0.5**2,n_samples)
l = np.concatenate((l1, l2), axis=0)
print len(l)
# http://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
hist, bin_edges = np.histogram(l, bins=np.arange(-5,5), density=True)

print hist
print bin_edges

import matplotlib.pyplot as plt
from sklearn import mixture

fig, ax = plt.subplots()

print len(hist)
ax.plot(range(0,len(hist)), hist)


# http://scikit-learn.org/stable/modules/generated/sklearn.mixture.GMM.html
clf = mixture.GMM(n_components=2, covariance_type='full')
clf.fit(l)

for i in range(2):
    
print clf.weights_
print clf.means_
print clf.covars_


plt.show()
