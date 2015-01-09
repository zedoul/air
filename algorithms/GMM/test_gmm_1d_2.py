from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib.mlab
import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))


yourdata = []
for i in range(10):
    for j in range(i):
        yourdata.append(i)

cov_types = ["spherical", "tied", "diag", "full"]
clf = mixture.GMM(n_components=1, covariance_type=cov_types[3], params="wmc")
clf.fit(yourdata)
m1 = clf.means_
w1 = clf.weights_
c1 = clf.covars_

print yourdata

histdist = plt.hist(yourdata, 10, normed=1, facecolor='green', alpha=0.5)
print len(histdist[1])

#plotgauss1 = lambda x: plt.plot(x, w1*matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0], linewidth=3)
#plotgauss2 = lambda x: plt.plot(x, w2*matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0], linewidth=3)
print histdist[1]
print type(histdist[1])
#plotgauss1(histdist[1])

plt.plot(histdist[1],w1*matplotlib.mlab.normpdf(histdist[1],m1,np.sqrt(c1))) 

#plotgauss2(histdist[1])
#plt.subplots_adjust(left=0.15)
plt.show()
