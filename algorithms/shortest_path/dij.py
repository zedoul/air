import heapq
def shortest_path(G, start, end):
   def flatten(L):
      while len(L) > 0:
         yield L[0]
         L = L[1]
   q = [(0, start, ())]
   visited = set()
   while True:
      (cost, v1, path) = heapq.heappop(q)
      if v1 not in visited:
         visited.add(v1)
         if v1 == end:
            return list(flatten(path))[::-1] + [v1]
         path = (v1, path)
         for (v2, cost2) in G[v1].iteritems():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2, v2, path))
G = {'A': {'C': 3, 'B': 1, 'D': 7}, 'C': {'A': 3, 'B': 42, 'E': 13, 'D': 2}, 'B': {'A': 1, 'C': 42, 'E': 27, 'D': 6}, 'E': {'C': 13, 'B': 27, 'D': 5}, 'D': {'A': 7, 'B': 6, 'E': 5}}
print ' '.join(shortest_path(G,'A','E'))
