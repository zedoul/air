def getMinHeight(l,basis):
	ret = 0
	for i in range(len(l)):
		if i < basis:
			continue
		if int(l[i]) == 1: break;
		else: ret=ret+1;
	return ret

def wideroom(m,w,h):
	ret = 0
	for b in range(h):
		for left in range(w):
			minHeight = getMinHeight(m[left],b)
			for h in range(w-left):
				right = h+left
				minHeight = min(minHeight, getMinHeight(m[right],b))
				ret = max(ret, ((right-left+1)*minHeight))
	return int(ret)

size = raw_input().split(' ')
pmap = []
for i in range(int(size[0])):
	pmap.append(list(''.join(str(raw_input()).split())))
print wideroom(zip(*pmap), int(size[1]), int(size[0]))
