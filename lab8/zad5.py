#A map of the country is given in the form of the graph G = (V, E). The driver wants to pass
# from city (vertex) s to city t. Unfortunately, some roads (edges) are tolled. Every road has one
#the unit fee itself. Please enter some algorithm that finds the route that requires the lowest possible number
# floss. Generally, G is directed, but you can indicate an algorithm for an undirected graph first.
#BFS with the fact that if the road is free, we put the vertex at the beginning of the queu#e

import collections
def cheapest_path(G,S,F):
    parent=[None for i in range(len(G))]
    deq=collections.deque([S])
    visited=[False for i in range(len(G))]
    visited[S]=True
    while deq:
        u=deq.pop()
        for v in G[u]:
            if not visited[v[0]]:
                visited[v[0]]=True
                parent[v[0]] = u
                if v[1]==0:
                    deq.appendleft(v[0])
                else:
                    deq.append(v[0])

    path=[F]
    while F!=S:
        F=parent[F]
        path.append(F)

    return path[::-1]
