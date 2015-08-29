m1 = m2 = NULL

m1 = cbind(m1, c(1,2,3,4,5))
m1 = cbind(m1, c(1,2,3,4,5))
m1 = cbind(m1, c(1,2,3,4,5))

m2 = cbind(m2, c(11,21,31,41,51))
m2 = cbind(m2, c(11,21,31,41,51))
m2 = cbind(m2, c(11,21,31,41,51))

r1 = apply(m1,1,mean)
r2 = apply(m2,1,mean)
