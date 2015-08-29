'''
a^2 + b^2 = c^2 is equivalent to 0 = a(b-1000) - 1000b + 500,000.
'''
for b in xrange(1,998):
    a = (1000*b - 500000) / (b-1000.0)
    if a == int(a) :
        print int(a * b * (1000 - a - b))
        break
