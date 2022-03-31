#A map of the country is given in the form of the graph G = (V, E), where the vertices are
#cities and edges are roads that connect cities. The length of each road is known (expressed in kilometers as a natural number). Alicja and Bob take (alternately) a bus from the city of x ∈ V to the city of y ∈ V,
#driving in each subsequent city. Alicja chooses the route and decides who is leading first.
#Please suggest an algorithm that indicates such a route (and the person who is to drive first) so that
#Alicja traveled as few kilometers as possible. The algorithm should be as fast as possible (but most of all
#correct).

from queue import PriorityQueue

def grande_strategia(G,s,f):
    n = len(G)
    inf = float('inf')
    q = PriorityQueue()
    d = [inf for i in range(2*n)]
    d[2*s],d[2*s+1] = 0,0
    visited = [False for i in range(2*n)]
    q.put((0,2*s))
    q.put((0,2*s+1))
    while not q.empty():
        tmp,u = q.get()
        if visited[u]!=True:
            visited[u]=True
            for v in range(n):
                if G[u//2][v] > 0:
                    if u%2==0:
                        if visited[2*v+1] == False and d[2*v+1] > d[u] + G[u//2][v]:
                            d[2*v+1] = d[u]+G[u//2][v]
                            q.put((d[2*v+1],2*v+1))
                    else:
                        if visited[2*v] == False and d[2*v] > d[u]:
                            d[2*v] = d[u]
                            q.put((d[2*v],2*v))

    return min(d[2*f],d[2*f+1])
