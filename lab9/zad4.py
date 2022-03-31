#We have a given graph G = (V, E) with weights w∶ E → N− {0} (positive natural numbers).
#We want to find the path from vertex u to v so that the product of the weights is minimal. Discuss the solution (without
#implementation)

def min_product(G,a,w):
    n=len(G)
    inf = float('inf')
    d=[inf for i in range(n)]
    d[a]=0
    parent=[None for i in range(n)]
    visited=[False for i in range(n)]
    for i in range(n):
        u = dis(d, visited, n)
        visited[u] = True
        for v in G[u]:
            if visited[v[0]] == False and d[v[0]] > d[u] + math.log(v[1]):
                d[v[0]] = d[u] + math.log(v[1])
                parent[v[0]]=u
    path=[]
    x=w
    while x!=a:
        path.append(x)
        if parent[x]!=None:
            x=parent[x]

    path.append(a)


    return path[::-1]
