#There is a table of exchange rates. For every two currencies x and y an entry
#K [x] [y] means how much currency x has to be paid to get the currency unit y. Please suggest al-
#a gorym that checks if there is a currency z that a unit of z can get more than a unit of z
#through a series of currency exchanges.

import math

def modified_bel(G,s):
    inf = float('inf')
    d = [inf for i in range(s+1)]
    d[s] = 0
    for i in range(s+1):
        for edge in G:
            if d[edge[1]] > d[edge[0]] + edge[2]:
                d[edge[1]] = d[edge[0]] + edge[2]


    for edge in G:
        if d[edge[1]] > d[edge[0]] + edge[2]:
            return True

    return False

def trade(A):
    G=[]
    n=len(A)
    for i in range(n):
        G.append((A[i][0],A[i][1],(math.log(1/A[i][2]))))

    k=0

    for i in range(n):
        k=max(k,G[i][0],G[i][1])

    for i in range(k+1):
        G.append((k+1,i,0))

    return modified_bel(G,k+1)
