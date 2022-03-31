#Please implement the BFS algorithm so that it finds
#the shortest paths in the graph and then to be able to write the shortest path from the given starting point
#to the indicated vertex.

def shortest_path(G,S,F):
    parent=[None for i in range(len(G))]
    q=Queue()
    visited=[False for i in range(len(G))]
    q.put(S)
    visited[S]=True
    while not q.empty():
        u=q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                parent[v]=u
                q.put(v)

    path=[F]
    print(path)
    while F!=S:
        if parent[F]==None:
            return None
        F=parent[F]
        path.append(F)

    return path[::-1]
