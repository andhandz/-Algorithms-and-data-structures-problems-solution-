#In one country with N cities, it was decided to merge
#all cities with a motorway network, so that it is possible to reach every city by motorway. Because
#the continent on which the country lies is flat, the location of each city is described by two
#√ numbers x, y, and distance
#in a straight line between cities, the number of kilometers is expressed by the formula: len = (x 1 - x 2) 2 + (y 1 - y 2) 2.
#Due to the savings in materials, the motorway connects two cities in a straight line.
#As the presidential election is approaching, all highways have been built simultaneously and as a target
#it was decided to minimize the time between the opening of the first and last highway. Construction time of the car
#the strada expressed in days is equal to ⌈len⌉ (the ceiling of the motorway length expressed in km). Please suggest
#an algorithm that determines the minimum number of days between the opening of the first and the last motorway.

import math

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

def Krus(edges,c,i):
    Ar = []
    n=len(edges)
    for j in range(n):
        Ar.append(Node(j))

    z=edges[i][2]
    diff=float('inf')
    while c < n - 1:
        x, y = find(Ar[edges[i][0]]), find(Ar[edges[i][1]])
        if x != y:
            diff=edges[i][2]-z
            union(x, y)
            c += 1
        i += 1
        if i == len(edges) and c < n - 1: return float('inf')

    return diff

def highway(A):
    n=len(A)
    G=[]
    for i in range(n):
        for j in range(i+1,n):
            leng=int(math.sqrt((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2))+1
            G.append((i,j,leng))

    G.sort(key=lambda x:x[2])
    m=len(G)
    diff=float('inf')
    for i in range(m-n+1):
        diff=min(Krus(G,i,i),diff)

    return diff
