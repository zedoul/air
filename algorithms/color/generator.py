import random
for i in range(2000):
    x = random.randint(0, 16777215)
    print "\"#%06x\"," % x
