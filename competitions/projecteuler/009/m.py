for b in xrange(1,998):
    a = (1000*b - 500000) / (b-1000.0)
    if a == int(a) :
        print int(a * b * (1000 - a - b))
        break
