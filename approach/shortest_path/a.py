def track_past_city(x,y):
    return (x[0]+y[0],x[1:]+y[1:]) #0 is how far you've gone, #[1:] is where you've been

def shortestPath(Cities,Distances):
    if len(Cities)==1: return 0, Cities[0]
    else: return min( map( lambda n: (track_past_city((Distances[Cities[0],Cities[n]],Cities[0]),shortestPath(Cities[n:],Distances))), range(1,len(Cities))) )
#    else: return min( map( lambda n: (track_past_city((Distances[Cities[0],Cities[n]],Cities[0]),shortestPath(Cities[n:],Distances))), [1]) )


d  = {("A","A"):0, ("A","B"):1, ("A","C"):3, ("A","D"):7 , ("A","E"):101,
           ("B","A"):101, ("B","B"):0, ("B","C"):42, ("B","D"):6, ("B","E"):27,
           ("C","A"):101, ("C","B"):101, ("C","C"):0, ("C","D"):2, ("C","E"):13,
           ("D","A"):101, ("D","B"):101, ("D","C"):101, ("D","D"):0, ("D","E"):5,
           ("E","A"):101, ("E","B"):101, ("E","C"):101, ("E","D"):101, ("E","E"):0
    }

print d["A","A"]

print shortestPath(["A","B", "C", "D", "E"],d)
