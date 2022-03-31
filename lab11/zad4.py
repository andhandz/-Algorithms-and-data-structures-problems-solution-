#Please enter the algorithm that the tree computes with as input
#association with maximum cardinality. Will the algorithm still work if every edge has
#positive weight and we are looking for an association with the maximum sum of weights?

from queue import Queue


def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n
    visited[s] = True

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()

        for v in range(n):
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                q.put(v)

    return visited[t]



def BFS2(G, s):
    q = Queue()
    visited = [False] * len(G)
    color = [-1] * len(G)

    q.put(s)
    visited[s] = True
    color[s] = 1  # 1 kolor

    while not q.empty():
        u = q.get()

        for v in range(len(G)):
            if u != v and G[u][v] == 1 and not visited[v]:
                visited[v] = True
                color[v] = 1 - color[u]
                q.put(v)

            if G[u][v] == 1 and u != v and color[u] == color[v]:
                return False

    return color


def fordFulkerson(G, s, t):
    n = len(G)
    parent = [None] * n
    maxFlow = 0

    while BFS(G, s, t, parent):
        u = t
        mini = float("inf")

        while u != s:
            if G[parent[u]][u] < mini:
                mini = G[parent[u]][u]
            u = parent[u]

        maxFlow += mini

        u = t
        while u != s:
            G[parent[u]][u] -= mini
            G[u][parent[u]] += mini
            u = parent[u]

    return maxFlow


def maxMatchingTree(G):
    n = len(G)
    G1 = [[0] * (n + 2) for _ in range(n + 2)]

    s = n 
    t = n + 1 

    color = BFS2(G, 0)  
    print(color)

    for u in range(n):
        for v in range(n):

            if G[u][v] == 1 and color[u] == 1 and color[v] == 0:
                G1[u][v] = G[u][v]
                G1[s][u] = 1  
                G1[v][t] = 1  

    for i in range(n + 2):
        print(G1[i])

    return fordFulkerson(G1, s, t)
