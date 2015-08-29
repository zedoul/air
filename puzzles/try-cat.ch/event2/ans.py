def nextIndex(data,i,w):
	return filter(
			lambda x:
			x+i>=0 and 
			x+i<w*w and 
			not (i%w==0 and x==-1) and
			not (i%w==w-1 and x==1) and
			data[x+i]==data[i]+1,
			[-3,-1,1,3]
			)

def _snakegame(data,i,w):
	return map(
			lambda n:
			_snakegame(data,n+i,w)+[data[n+i]],
			nextIndex(data,i,w)
		)

def snakegame(data,i,w):
	return map(
			lambda n:
			_snakegame(data,n,w)+[data[n]],
			range(i,w*w)
		)

def flatten(l):
	    return reduce(lambda x,y: x+[y] if type(y) != list else x+flatten(y), l,[])

inp = []
w = raw_input().split(' ')
x = w 
for i in range(len(w)-1):
	x = raw_input().split(' ')
	for t in x:
		inp.append(int(t))
for t in x:
	inp.append(int(t))

lofl = max(snakegame(inp,0,len(w)))
ret = flatten(lofl)
ret.reverse()
print ' '.join(map(str, ret))

