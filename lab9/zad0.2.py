#Please implement the algorithm of your choice for calculating the minimum tree
#pin for the graph representation selected by the lecturer.

class Node:
    def __init__(self,val):
        self.val=val
        self.rank=0
        self.parent=self

def find(x):
    if x!=x.parent:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank: y.rank+=1


def Kruskal(G):
    edges=[]
    n=len(G)
    for u in range(n):
        for v in G[u]:
            val=v[1]
            if v[0]>u:
                edges.append((u,v[0],val))

    edges.sort(key=lambda x: x[2])
    c,i=0,0
    mst=[]
    Ar=[]
    for j in range(n):
        Ar.append(Node(j))
    print(edges)
    while c<n-1:
        x,y=find(Ar[edges[i][0]]),find(Ar[edges[i][1]])
        if x!=y:
            mst.append(edges[i])
            union(x,y)
            c+=1
        i+=1
        if i==len(edges) and c<n-1: return False

    return mst
