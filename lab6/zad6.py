#A rooted tree T is given, where every vertex v has-
#potentially negative — value (v). Please suggest an algorithm which finds the value the most
#value path in the tree T.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.bestPath = 0


def findBestPath(v):
    if v == None:
        return (0, 0)

    bestL, L = findBestPath(v.left)
    bestR, R = findBestPath(v.right)

    v.bestPath = max(0, v.val, v.val + L, v.val + R)

    best = max(v.bestPath, bestL, bestR, L + R + v.val)

    return (best, v.bestPath)


def returnBestPath(v):
    return max(findBestPath(v))
