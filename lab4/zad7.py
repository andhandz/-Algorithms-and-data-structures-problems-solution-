#An array A is given containing n elements each having one of the k colors. Pro-
#I am going to give the fastest possible algorithm that finds the indices i and j such that among the elements
#A [i], A [i + 1],. . . , A [j] are all k colors and the value of j - i is minimal (in other words,
#we are looking for the shortest range with all colors).

def colors(A,k):
    C=[0]*k
    i,j=0,1
    c=1
    best=len(A)
    s,f=0,len(A)-1
    C[A[0]]+=1
    p=0
    while j<len(A) and i<j:
        if p==0:
            C[A[j]]+=1
            if C[A[j]]==1:
                c+=1
        p = 0
        if c==k:
            p+=1
            if j-i+1<best:
                best=j-i+1
                s=i
                f=j
            C[A[i]]-=1
            if C[A[i]]==0:
                c-=1
            i += 1
            j-=1
        j+=1

    return s,f
