#Given is a set of points X = {x 1,. . . , x n} on
#straight. Please provide an algorithm that finds the minimum number of closed unit intervals,
#needed to cover all points with X. (Example: If X = {0.25, 0.5, 1.6} then you need two
#intervals, e.g. [0.2, 1.2] and [1.4, 2.4]).

def compartments(X):
    n=len(X)
    i=0
    c=0
    while i<n:
        beg=X[i]
        c+=1
        j=i+1
        while j<n and X[j]-beg<=1:
            j+=1

        i=j

    return c
