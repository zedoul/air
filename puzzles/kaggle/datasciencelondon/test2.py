import numpy as np
from sklearn import preprocessing as pp
from sklearn import cross_validation as cv
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC
import matplotlib.pylab as plt

workDir = "./data/"

# Read data
train = np.genfromtxt(open(workDir + 'train.csv','rb'), delimiter=',')
target = np.genfromtxt(open(workDir + 'trainLabels.csv','rb'), delimiter=',')
test = np.genfromtxt(open(workDir + 'test.csv','rb'), delimiter=',')
# Scale data
train = pp.scale(train)
test = pp.scale(test)
# Select features
selector = ExtraTreesClassifier(compute_importances=True, random_state=0)
plt.plot(train)
plt.savefig('train3.png')
plt.close()
print len(train)
print len(train[0])
train = selector.fit_transform(train, target)
plt.plot(train)
plt.savefig('train4.png')
plt.close()
print len(train)
print len(train[0])

print "====="
print len(test)
print len(test[0])
test = selector.transform(test)
print len(test)
print len(test[0])

# Estimate score
classifier = SVC(C=8, gamma=0.17)
scores = cv.cross_val_score(classifier, train, target, cv=30)
print scores
print('Estimated score: %0.5f (+/- %0.5f)' % (scores.mean(), scores.std() / 2))

# Predict and save
result = classifier.fit(train, target).predict(test)
idcol = np.arange(start=1,stop=9001)
result = np.column_stack((idcol,result))
np.savetxt(workDir + 'result.csv', result, fmt='%d',delimiter=",")
