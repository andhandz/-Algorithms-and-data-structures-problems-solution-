def quickselect(A,a,b,k):
    if k>0 and k<=b-a+1:
        ind=partition(A,a,b)
        if ind==a+k-1:
            return A[ind]
        if ind> a+k-1:
            return quickselect(A,a,ind-1,k)
        return quickselect(A,ind+1,b,k+a-ind-1)
    return False
