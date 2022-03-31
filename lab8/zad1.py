#Please implement the following algorithms:
#1. Checking if the graph is bipartite (ie note it is 2-color and use DFS or BFS).
#2. Count the number of connected components in the graph (implementation opposite to that of the previous task)

#1
def isBipartite(G,S):
    n=len(G)
    teams=[-1 for i in range(n)]
    visited=[False for i in range(n)]
    q=Queue()
    q.put(S)
    visited[S]=True
    teams[S]=1
    while not q.empty():
        u=q.get()
        for v in G[u]:
            if teams[v]==teams[u]:
                return False
            if teams[v]==-1:
                teams[v]=(teams[u]+1)%2
            if not visited[v]:
                visited[v]=True
                q.put(v)

    return True
    
#2
def DFS_matrix(G,S):
    n=len(G)
    time=[0]*n
    visited=[False for i in range(n)]
    c=0
    def dfs_visit(u):
        nonlocal G,visited,c
        visited[u]=True
        for i in range(n):
            if not visited[i] and G[u][i]==1:
                dfs_visit(i)
        time[u]=(c,u)
        c+=1

    dfs_visit(S)
    for i in range(n):
        if visited[i]==False:
            dfs_visit(i)
    G1=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]==1:
                G1[j][i]=1

    G=G1

    time.sort(reverse=True)
    for i in range(n):
        visited[i]=False

    sss=[]
    ar=[]
    time1=time.copy()
    for i in range(n):
        if visited[time1[i][1]]==False:
            if len(ar)>0:
                sss.append(ar)
            ar=[]
            dfs_visit(time1[i][1])
        ar.append(time1[i][1])

    if len(ar) > 0:
        sss.append(ar)
    return sss
