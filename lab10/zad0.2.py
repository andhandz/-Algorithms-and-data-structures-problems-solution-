#Please implement an algorithm that calculates the closure of
#chapters of a graph represented in a matrix form (a transitive closure of G, is the graph over this
#the same set of vertices, which for every two vertices u and v has an edge z u to v then i
#only if there is a path from u to v in G.

def BFS(G,S):
    q=Queue()
    visited=[False for i in range(len(G))]
    q.put(S)
    visited[S]=True
    while not q.empty():
        u=q.get()
        for v in range(len(G)):
            if not visited[v] and G[u][v]==1:
                visited[v]=True
                q.put(v)
                G[S][v]=1

def transitive_closure(G):
    for i in range(len(G)):
        BFS(G,i)

    return G
