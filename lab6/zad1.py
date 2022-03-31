#The Black Forest is a forest that grows on a number line somewhere in the south of England. Forest
#consists of n trees growing at positions 0,. . . , n - 1. For every i ∈ {0,. . . , n - 1} the gain c i, y, is known
#can be achieved by felling a tree from i. John Lovenoses wants to get the maximum profit from the felling
#trees, but it is forbidden by law to fell two trees in a row. Please propose an algorithm by which
#John will find the optimal cutting plan.

def forest(A):
    n=len(A)
    x2=A[0]
    x1=max(A[0],A[1])
    for i in range(2,n):
        x1,x2=max(x2+A[i],x1),x1

    return x1
