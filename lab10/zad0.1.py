#The graph G = (V, E) is given, where each edge has a weight
#from the set {1,. . . , ∣E∣} (the edge weights are pairwise different). Please propose an algorithm that for the data
#of the vertices x and y computes the path with the smallest sum of weights that leads from x to y along the edges of o
#decreasing weights (if there is no path, we return ∞).

def decreasing_path(graph, start, t):
    m = len(graph)
    n = 0
    for i in range(m):
        n = max(n, graph[i][0], graph[i][1])
    n += 1

    graph.sort(key=lambda x: x[2], reverse=True)

    shortest = [float('inf') for _ in range(n)]
    parent = [[] for _ in range(n)]
    shortest[start] = 0
    for i in range(m):
        u, v, w = graph[i]
        if shortest[u] + w < shortest[v]:
            shortest[v] = shortest[u] + w
            parent[v].append([u, w, shortest[v]])
        elif shortest[v] + w < shortest[u]:
            shortest[u] = shortest[v] + w
            parent[u].append([v, w, shortest[u]])

    if not parent[t]:
        return []
    result = [t]
    prev_val = shortest[t]
    prev_edge = parent[t][len(parent[t]) - 1][1]
    t = parent[t][len(parent[t]) - 1][0]
    while parent[t]:
        result.append(t)
        i = len(parent[t]) - 1
        u, w, s = parent[t][i]
        while prev_val - prev_edge != s:
            i -= 1
            u, w, s = parent[t][i]
        prev_val = s
        prev_edge = w
        t = u
    result.append(start)
    return result[::-1]
