#How to find shortest paths from vertex s to all others in an acyclic directed graph?

def Topological_sorting(G):
    n = len(G)
    visited = [False for i in range(n)]
    order = []
    def dfs_visit(u):
        nonlocal G, visited
        visited[u] = True
        for v in G[u]:
            if not visited[v[0]]:
                dfs_visit(v[0])
        order.append(u)

    for i in range(n):
        if visited[i]==False:
            dfs_visit(i)

    return order[::-1]

def shortest_path_dag(G,s):
    n=len(G)
    order=Topological_sorting(G)
    Edges=[]
    c=0
    inf = float('inf')
    while order[c]!=s:
        c+=1

    for i in range(c,n):
        for j in range(len(G[order[i]])):
            Edges.append((order[i],G[order[i]][j][0],G[order[i]][j][1]))

    d=[inf for i in range(n)]
    d[s]=0
    for edge in Edges:
        if d[edge[1]] > d[edge[0]] + edge[2]:
            d[edge[1]] = d[edge[0]] + edge[2]


    return d
