from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib.mlab
import numpy as np

#yourdata = []
#for i in range(100):
#    for j in range(i):
#        yourdata.append(i)

#yourdata = []
#for i in range(10):
#    yourdata.append(1)
#
#for i in range(10):
#    yourdata.append(100)

yourdata = []
for i in range(100):
    yourdata.append(100)


cov_types = ["spherical", "tied", "diag", "full"]
clf = mixture.GMM(n_components=3, covariance_type=cov_types[0], params="wmc")
clf.fit(yourdata)
m1,m2,m3 = clf.means_
w1,w2,w3 = clf.weights_
c1,c2,c3 = clf.covars_

print yourdata

sample = 100

plt.subplot(2, 1, 1)
histdist = plt.hist(yourdata, sample, normed=1, facecolor='green', alpha=0.3)

minval = min(yourdata)
maxval = max(yourdata)
print minval
print maxval
margin = (maxval-minval) / 20.0

plt.subplot(2, 1, 2)
xs = np.linspace(minval-margin,maxval+margin,sample*100)
ys = [matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0]*w1 + matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0]*w2 + matplotlib.mlab.normpdf(x,m3,np.sqrt(c3))[0]*w3 for x in xs]
plt.plot(xs,ys,color='y', lw=5)

xs = np.linspace(minval-margin,maxval+margin,sample*10)
ys = [matplotlib.mlab.normpdf(x,m1,np.sqrt(c1))[0]*w1 for x in xs]
plt.plot(xs,ys,color='r',lw=1)

xs = np.linspace(minval-margin,maxval+margin,sample*10)
ys = [matplotlib.mlab.normpdf(x,m2,np.sqrt(c2))[0]*w2 for x in xs]
plt.plot(xs,ys,color='g',lw=1)

xs = np.linspace(minval-margin,maxval+margin,sample*10)
ys = [matplotlib.mlab.normpdf(x,m3,np.sqrt(c3))[0]*w3 for x in xs]
plt.plot(xs,ys,color='b', lw=1)


print "----"
print m1
print m2
print m3
print c1
print c2
print c3
print w1
print w2
print w3
plt.show()

