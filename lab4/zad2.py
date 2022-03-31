#An array A of length n is given. The values ​​in the array come from the set B, where ∣B∣ = log n.
#Please propose the fastest possible sorting algorithm for the A table

def binsearch(A,a,b,v):
    if b-a==1:
        if A[a]==v:
            return True
        return False
    if binsearch(A,a,(a+((b-a)//2)),v) or binsearch(A,(a+((b-a)//2)),b,v):
        return True
    return False

def repair(A,k):
    p=k
    while p!=0 and A[p]<A[p-1]:
        A[p],A[p-1]=A[p-1],A[p]
        p-=1


import math
def logsort(A):
    n=len(A)
    Av=[0]*math.ceil(math.log(n))
    k=0
    for i in range(n):
        if binsearch(Av,0,len(Av),A[i])==False:
            Av[k]=A[i]
            repair(Av,k)
            k+=1
    m=0
    for i in range(len(Av)):
        for j in range(m,len(A)):
            if A[j]==Av[i]:
                A[m],A[j]=Av[i],A[m]
                m+=1

    return A
