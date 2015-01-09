from sklearn import mixture
import matplotlib.pyplot as plt
import matplotlib.mlab
import numpy as np

yourdata = []
for i in range(10):
    yourdata.append(1)

for i in range(10):
    yourdata.append(100)

cov_types = ["spherical", "tied", "diag", "full"]
clf = mixture.GMM(n_components=3, covariance_type=cov_types[0], params="wmc")
clf.fit(yourdata)
m1,m2,m3 = clf.means_
w1,w2,w3 = clf.weights_
c1,c2,c3 = clf.covars_

print clf.score([0])
print clf.score([30])
print clf.score([60])
print clf.score([90])
print clf.score([100])
print clf.score([105])
