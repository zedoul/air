import sys
def maxshuffle(a,b):
	return sorted(a+b,key=lambda p: int(p), reverse=True)
data = raw_input().split(' ')
ret = maxshuffle(list(str(data[0])),list(str(data[1])))
print ''.join(ret)

