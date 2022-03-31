#Each brick is an interval of characters [a, b]. A sequence of blocks is given [a 1, b 1],
#[a 2, b 2],. . ., [a n, b n]. The blocks fall on the number line in the order given in the sequence. Please suggest
#an algorithm that calculates how many blocks should be removed from the list so that each successive falling block can fit
#all in there that fell right in front of him.

def blocks(A):
    n=len(A)
    F=[1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j][0]<=A[i][0] and A[j][1]>=A[i][1] and F[j]+1>F[i]:
                F[i]=F[j]+1
    print(F)
    return n-max(F)
