#Please implement the Dijkstra algorithm (for the graph representation chosen by the tutor).

def relax(u,v):
    if v.d>u.d+w(u,v):
        v.d=v.d+w(u,v)
        v.parent=u

import math

def dis(d,visited,n):
    inf = float('inf')
    mini=inf
    j=-1
    for i in range(n):
        if visited[i]==False and d[i]<mini:
            mini=d[i]
            j=i

    if j==-1:return False
    return j

def Djikstra_mat(G,s):
    n=len(G)
    inf=float('inf')
    d=[inf for i in range(n)]
    d[s]=0
    visited=[False for i in range(n)]
    for i in range(n):
        u=dis(d,visited,n)
        visited[u]=True
        for v in range(n):
            if G[u][v]>0 and visited[v]==False and d[v]>d[u]+G[u][v]:
                d[v]=d[u]+G[u][v]

    return d
