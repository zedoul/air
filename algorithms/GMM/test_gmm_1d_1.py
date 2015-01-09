from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib.mlab
import numpy as np


gmm = mixture.GMM(2, n_iter=1)
gmm.means_ = np.array([[-1], [3]])
gmm.covars_ = np.array([[1.5], [0.5]]) ** 2
gmm.weights_ = np.array([0.5, 0.5])

yourdata = gmm.sample(10000)


clf = mixture.GMM(n_components=2, covariance_type='full')
clf.fit(yourdata)
m1, m2 = clf.means_
w1, w2 = clf.weights_
c1, c2 = clf.covars_

histdist = plt.hist(yourdata, 1000, normed=True)

plotgauss1 = lambda x: plt.plot(x,w1*matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0], linewidth=3)
plotgauss2 = lambda x: plt.plot(x,w2*matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0], linewidth=3)
plotgauss1(histdist[1])
plotgauss2(histdist[1])

plt.show()
