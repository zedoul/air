import numpy as np

a = np.matrix('1 2; 3 4')
a = np.matrix([[1 2] [3 4]])
b = np.matrix('2 1; 4 4') # Only one same element
c = np.matrix('2 1; 4 3') # There is no same element
d = np.matrix('1 2; 3 4') # There is no same element

assert (True == (a == b).any() ) 
assert (False == (a == c).any() ) 
assert (True == (a == d).all() ) 


