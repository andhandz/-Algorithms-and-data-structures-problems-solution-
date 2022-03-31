#We have two arrays, A [n] and B [n]. Should be found
#the length of their longest common substring. (Classic O (n 2) dynamic algorithm).

def lcs(A,B):
    n,m=len(A),len(B)
    C=[[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                C[i][j]=C[i-1][j-1]+1
            else:
                C[i][j]=max(C[i-1][j],C[i][j-1])

    return C[n][m]
