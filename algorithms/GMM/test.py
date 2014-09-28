# http://www.experimentalnotes.co.uk/blog/programming/double-gaussian-fitting/
# http://scikit-learn.org/stable/modules/generated/sklearn.mixture.GMM.html
import numpy as np
import matplotlib.pyplot as plt
from sklearn import mixture
import matplotlib.pyplot
import matplotlib.mlab
 
samples = 100000
data = np.zeros(samples)
 
mu, sigma = 0.05, 0.015
data[0:samples/2] = np.random.normal(mu, sigma, (samples/2))
mu, sigma = 0.18, 0.01
data[(samples/2):samples] = np.random.normal(mu, sigma, (samples/2))
clf = mixture.GMM(n_components=2, covariance_type='full', min_covar=0.00001)
 
clf.fit(data)
 
m1, m2 = clf.means_
w1, w2 = clf.weights_
c1, c2 = clf.covars_
 
# show lables 
plt.ylabel("Frequency")
plt.xlabel("x")

# show hist
histdist = plt.hist(data, 100, normed=True, alpha=0.2)

# show gausses
plotgauss1 = lambda x: plt.plot(x,w1*matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0], linewidth=2, color='k')
plotgauss2 = lambda x: plt.plot(x,w2*matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0], linewidth=2, color='r')
plotgauss1(histdist[1])
plotgauss2(histdist[1])

# predict
print str(clf.predict([0.05])) + " with " + str(clf.predict_proba([0.05]))
print str(clf.predict([0.20])) + " with " + str(clf.predict_proba([0.20]))
print str(clf.predict([0.13])) + " with " + str(clf.predict_proba([0.13]))

plt.show()

