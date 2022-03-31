#We say that the vertex t in the directed graph is universal
#an exit if (a) from every other vertex of v there is an edge from v to t, and (b) no edge exists
#starting from vol.
#1. Give the algorithm that finds a universal outlet (if any) in the matrix representation (O (n 2)).

def universal_sink(G):
    n = len(G)
    u, v = 0, 0

    while u < n and v < n:
        if G[u][v] == 0:
            v += 1
        else:
            u += 1

    if u == n:
        return 'doesnt exist'

    def is_sink(u):
        for v in range(n):
            if G[u][v] == 1:
                return False
            if u != v and G[v][u] == 0:
                return False

        return True

    if is_sink(u):
        return u
    else:
        return 'doesnt exist'
