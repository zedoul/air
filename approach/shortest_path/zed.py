def track (x,y):
	return x[1:]+y[1:]

def detect(target,index,w,graph):
	for a in [-1,1,-3,3]:
		if (index+a<0 || index+a>len(graph)-1):
			return False
		if (graph[index+a] != 
	return True

def snakegame(index,num,width,targets)
	nextTarget = filter(lambda x:(detect(x,index,width,targets)),targets)
	if (0 == len(nextTargets)):
		return num
	else:
		return max( map( lambda x:
					(track(
						snakegame(remains[x:],targets)
						)),
					4
				))

w = 3
c = [2,3,5,4,5,9,4,6,7]
snakegame(0,2,w,c):

