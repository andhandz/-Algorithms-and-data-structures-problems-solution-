#The Hamilton path is a path that passes through all of them
#vertices in the graph by each one exactly once. In the general graph, finding the Hamilton path is a pro
#with NP-hard metal. Please enter some algorithm that will find out if there is a Hamilton path in acyclic
#directed graph.

def hamilton_path(G):
    n=len(G)
    visited=[False for i in range(n)]
    result=[]
    def dfs_visit(v):
        nonlocal visited
        visited[v]=True
        for u in G[v]:
            if not visited[u]:
                dfs_visit(u)
        result.append(v)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    if len(result)!=n: return None
    for i in range(n-1,0,-1):
        u=result[i]
        v=result[i-1]
        found=False
        for w in G[u]:
            if w==v:
                found=True
                break
        if found==False: return None

    return result[::-1]
