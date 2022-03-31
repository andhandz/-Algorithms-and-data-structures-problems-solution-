#A sequence of closed intervals is given [a1, b1],. . . , [an, bn]. Please
#propose an algorithm that finds an interval [at, bt] that contains as many as possible
# other compartments.

def partition(A,p,r):
    x=A[r][0]
    i=p-1
    for j in range(p,r):
        if A[j][0]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]

    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def qsort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if q-p<=r-q:
            qsort(A,p,q-1)
            p=q+1
        else:
            qsort(A,q+1,r)
            r=q-1

    return A

def max_interval(A):
    n=len(A)
    B=[0]*n
    C=[0]*n
    B1=[0]*n
    C1=[0]*n
    for i in range(n):
        B[i]=(A[i][0],i)
        C[i]=(A[i][1],i)

    qsort(B,0,n-1)
    qsort(C,0,n-1)
    for i in range(n):
        B1[B[i][1]]=i
        C1[C[i][1]]=i

    max=0
    ind=0
    for i in range(n):
        if C1[i]-B1[i]>=max:
            if C1[i]-B1[i]>max or A[i][1]-A[i][0]>A[ind][1]-A[i][0]:
                max=C1[i]-B1[i]
                ind=i

    return A[ind]
