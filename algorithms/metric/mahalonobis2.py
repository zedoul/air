import numpy;
import scipy.spatial.distance;
s = numpy.array([[20,55,119],[123,333,11],[113,321,11],[103,313,191],[123,3433,1100]]);

covar = numpy.cov(s, rowvar=0);
if(s.shape[1:2]==(1,)):
    invcovar = numpy.linalg.inv(covar.reshape(1,1))
else:
    invcovar = numpy.linalg.inv(covar)

print s[0]
print s[1]
print scipy.spatial.distance.mahalanobis(s[0],s[1],invcovar);
