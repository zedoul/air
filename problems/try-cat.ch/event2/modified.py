def k(d,i,w):
	return map(lambda n:k(d,n+i,w)+[d[n+i]],
	filter(lambda x:x+i>=0 and x+i<w*w and not (i%w==0 and x==-1) and not (i%w==w-1 and x==1) and d[x+i]==d[i]+1,[-3,-1,1,3]))
def s(d,i,w):
	return map(lambda n:k(d,n,w)+[d[n]],range(i,w*w))
def f(l):return reduce(lambda x,y: x+[y] if type(y) != list else x+f(y), l,[])
p = []
w = raw_input().split(' ')
x = w 
for i in range(len(w)-1):
	x = raw_input().split(' ')
	for t in x:
		p.append(int(t))
for t in x:
	p.append(int(t))
l = max(s(p,0,len(w)))
r = f(l)
r.reverse()
print ' '.join(map(str,r))
