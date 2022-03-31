#The vertex of v in a directed graph is a good start if
#any other vertex can be reached by the directed path starting from v. Please enter which algorithm
#states whether a given graph is a good start.

def good_start(G):
    n = len(G)
    visited = [False for i in range(n)]
    order=[0 for i in range(n)]
    c=1
    def dfs_visit(u):
        nonlocal G, visited,c
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

        order[u]=c
        c+=1

    for i in range(n):
        if visited[i]==False:
            dfs_visit(i)

    visited=[False for i in range(n)]
    a=False
    for i in range(n):
        if order[i]==n:
            dfs_visit(i)
            a=i
            break

    for i in range(n):
        if visited[i]==False:
            return False

    return a
