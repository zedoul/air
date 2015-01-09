#Python code for computer practical 4

from scipy import*
from pylab import plot, show, figure, axis, step

#Generate a sample of size 1000 using PYTHON
n = 1000
# we shall sample directly from the bivariate Normal distribution;

mu = [0,0]
# setting the mean parameter 
cov = [[4,1],[1,4]]
# setting the covariance matrix 
x,y = random.multivariate_normal(mu,cov,n).T 

# plot the last 100 values as in Figure 4.1 on the notes.
step(x[900:],y[900:])
show()

# compute the estimate of P(X1 >= 0, X2 >= 0)
prob = zeros(n)
prob[0]= (x[0]>=0 and y[0]>=0)

for i in xrange(1,n):
   prob[i]= prob[i-1]+(x[i]>=0 and y[i]>=0)
y = prob/xrange(1,n+1)

# plotting the resulting probabilities.
plot(y)
axis([-200, n+200, 0.1, 0.4])
show()
