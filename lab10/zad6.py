#Given is an acyclic, connected undirected weighted graph T (i.e., T is
#in fact a weighted tree). Please indicate which algorithm finds the vertex T from which
#the distance to the farthest vertex is minimal.

def Djikstra_modified(G,s):
    inf = float('inf')
    n=len(G)
    d=[-inf for i in range(n)]
    d[s]=0
    visited=[False for i in range(n)]
    parent=[None for i in range(n)]
    for i in range(n):
        u=dis(d,visited,n)
        visited[u]=True
        for v in range(n):
            if G[u][v]>0 and visited[v]==False and d[v]<d[u]+G[u][v]:
                d[v]=d[u]+G[u][v]
                parent[v]=u

    m=0
    ind=0
    for i in range(n):
       if m<d[i]:
        m=d[i]
        ind=i

    path=[]
    while ind!=None:
        path.append(ind)
        ind=parent[ind]

    return m,path

def max_path(T):
    m=0
    path=[]
    for i in range(n):
        if Djikstra_modified(T,i)[0]>m:
            m,path=Djikstra_modified(T,i)

    k=0
    for i in range(len(path)-1):
        m-=T[path[i]][path[i+1]]
        if k>=m:
            return i
        k += T[path[i]][path[i + 1]]

    return path[len(path)-1]
