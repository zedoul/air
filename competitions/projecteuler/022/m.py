import time

def score(name):
    ret = 0
    for c in name:
        assert ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z')))
        ret += ord(c) - ord('A') + 1
    return ret

def NamesScores():
    with open("./p022_names.txt", 'r') as f:
        names = f.read().split(',')
        names.sort()

        ret = 0
        position = 1
        for name in names:
            name = name.strip('"')
            ret += score(name) * position
            position += 1
    f.close()
    return ret

start = time.time()
ret = NamesScores()
elapsed = (time.time() - start)
print "found %d in %s seconds" % (ret,elapsed)

