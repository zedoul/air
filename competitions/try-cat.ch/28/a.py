import sys
def cat(a,b):
	return sorted(a+b,key=lambda p: int(p))
ret = cat(raw_input().split(' '),raw_input().split(' '))
print ' '.join(ret)

