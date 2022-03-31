#The captain of a ship is wondering
#whether he can enter the port even though the tide has taken off. He has a map of the bay in the form of a table at his disposal
#M, where M [y] [x] is the bay depth at position (x, y). If it is greater than some int value T
#then the ship might end up there. Initially, the ship is in position (0, 0) and the port is in position
#(n - 1, m - 1). From that position, a ship can only proceed directly to the position immediately adjacent
#(that is, to a position where exactly one of the coordinates differs by one). Please write a function
#solving the captain's problem.

def ship(G,M,t,n,m):
    D=[0]*(n*m)
    k=0
    for i in range(n):
        for j in range(m):
            D[k]=M[i][j]
            k+=1

    q=Queue()
    l=m*n
    visited=[False for i in range(l)]
    q.put(S)
    visited[S]=True
    while not q.empty():
        u=q.get()
        for i in range(l):
            if G[u][i]==1 and D[u*m+i]>t:
                if not visited[i]:
                    visited[i]=True
                    q.put(i)

    return visited[n*m-1]
