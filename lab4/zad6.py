#An array A with n pairs of different numbers is given. Please suggest an algorithm that
#finds two numbers x and y of A, that y - x is as large as possible and there is no number z such in the array,
#that x <y <z (in other words, sorting the array A ascendingly would result in the numbers A [i] and A [i + 1] for
#of which A [i + 1] - A [i] is the greatest).

def maxspan(A):
    n=len(A)
    min_=A[0]
    max_=A[0]
    for i in range(n):
        min_= min(min_,A[i])
        max_= max(max_,A[i])

    B=[[] for i in range(n)]
    x= (max_+min_)/n

    for i in range(n):
        d=int((A[i]-min_)/x)
        B[d].append(A[i])

    result=0
    prev_max=max(B[0])
    for i in range(1,n):
        if len(B[i])!=0:
            act_min=min(B[i])
            result=max(result,act_min-prev_max)
            prev_max=max(B[i])

    return result
