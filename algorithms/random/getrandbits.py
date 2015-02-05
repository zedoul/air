import random

# https://docs.python.org/2/library/random.html#random.getrandbits
#
# Returns a python long int with k random bits. This method is supplied with the
# MersenneTwister generator and some other generators may also provide it as an 
# optional part of the API. When available, getrandbits() enables randrange() to
# handle arbitrarily large ranges.
r = random.getrandbits(3)
print bin(r)
