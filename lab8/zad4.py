#The graph G = (V, E) is given, where each edge has a weight from the set
#{1,. . . , ∣E∣} (the edge weights are pairwise different). Please propose an algorithm that for the given vertices
#x and y checks if there is a path from x to y in which we go over edges with increasingly lighter weights.

def exist(G,S,F,V):
    q=Queue()
    visited=[False for i in range(len(G))]
    q.put(S)
    visited[S]=True
    parent = [[] for i in range(len(G))]
    edge_vis=[[False for i in range(len(G))] for j in range(len(G))]
    while not q.empty():
        u=q.get()
        for v in G[u]:
            if edge_vis[u][v] == False:
                if len(parent[u])==0:
                    parent[v].append(u)
                    visited[v] = True
                    edge_vis[u][v],edge_vis[v][u]=True,True
                    q.put(v)
                for par in parent[u]:
                    if V[u][v]<V[par][u]:
                        parent[v].append(u)
                        visited[v]=True
                        edge_vis[u][v], edge_vis[v][u] = True, True
                        q.put(v)

    return visited[F]
