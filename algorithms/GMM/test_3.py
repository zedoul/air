from sklearn import mixture
import matplotlib.pyplot
import matplotlib.mlab
import numpy as np

samples = 100000
data = np.zeros(samples)
mu, sigma = 0.05, 0.015
data[0:samples/2] = np.random.normal(mu, sigma, (samples/2))
mu, sigma = 0.18, 0.01
data[(samples/2):samples] = np.random.normal(mu, sigma, (samples/2))
yourdata = data

clf = mixture.GMM(n_components=2, covariance_type='full')
clf.fit(yourdata)
m1, m2 = clf.means_
w1, w2 = clf.weights_
c1, c2 = clf.covars_
histdist = matplotlib.pyplot.hist(yourdata, 100, normed=True)
plotgauss1 = lambda x: matplotlib.pyplot.plot(x,w1*matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0], linewidth=3)
plotgauss2 = lambda x: matplotlib.pyplot.plot(x,w2*matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0], linewidth=3)
plotgauss1(histdist[1])
plotgauss2(histdist[1])

matplotlib.pyplot.show()
