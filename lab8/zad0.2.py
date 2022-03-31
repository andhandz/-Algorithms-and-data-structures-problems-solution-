#G is given an undirected graph with n vertices. Suggest
#an algorithm that determines whether there is a cycle in G consisting of exactly 4 vertices. We assume that
#the graph is represented by the neighborhood matrix A.

def cycle4(G):
    n=len(G)
    q=[]
    neigh=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]==1:
                neigh[i].append(j)
    def dfs_visit(G,u,q):
        nonlocal neigh
        q.append(u)
        for i in range(n):
            x=1
            if len(q)>1: x=2
            if G[u][i]==1 and q[len(q)-x]!=i:
                G[u][i]=0
                dfs_visit(G,i,q)

        if len(q)>=5:
            for i in range(len(neigh[q[len(q)-1]])):
                if neigh[q[len(q)-1]][i]==q[len(q)-4] and q[len(q)-1]==q[len(q)-5]:
                    print("cykl:",q[len(q)-5:len(q)])
        del q[len(q)-1]


    dfs_visit(G,0,q)
