#We have a series of water containers, connected (each to each) by pipes.
#The containers have the shape of rectangles, the pipes have no volume (area). Each container is described
#by the coordinates of the upper left corner and the lower right corner.
#We know that A "surface" of water was poured into the containers (of course, the water flowed through pipes to the lowest
#containers). Please propose an algorithm that calculates how many containers were fully flooded.

def partition(A,p,r):
    x=A[r][0][1]
    i=p-1
    for j in range(p,r):
        if A[j][0][1]<=x:
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

def capacity(x,h):
    if x[0][1]<=h:
        return (x[1][0]-x[0][0])*(x[0][1]-x[1][1])
    return (x[1][0]-x[0][0])*(h-x[1][1])

def containers(T,A):
    n=len(T)
    qsort(T,0,n-1)
    i=0
    print(T)
    while i<n and A>=0:
        A-=capacity(T[i],T[i][0][1])
        j=i+1
        An=A
        while j<n and T[j][1][1]<T[i][0][1]:
            A-=capacity(T[j],T[i][0][1])
            j+=1

        if A<0:
            return i
        A=An
        i+=1

    return n
