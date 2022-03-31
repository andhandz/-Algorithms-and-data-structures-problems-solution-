#The well-known mobile operator Pause decided to terminate its activities in
#Poland. One of the main elements of the entire procedure is to turn off all broadcasting stations (which
#creates a coherent graph of connections). Due to technological reasons, the devices should be switched off individually and the operation
#the rator also cares about the fact that all subscribers within range during the entire process
#working stations could connect with each other (i.e. so that the graph remains consistent). Please propose an algorithm
#giving the order in which the stations are turned off.

def rm_order(G,S):
    n=len(G)
    visited=[False for i in range(n)]
    order=[]
    def dfs_visit(u):
        nonlocal G,visited
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(v)

        order.append(u)

    dfs_visit(S)
    return order
