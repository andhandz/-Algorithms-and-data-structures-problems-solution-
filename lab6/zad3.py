#There is a table A [n] with the lengths of cars that stand in the queue,
#to board the ferry. The ferry has two lanes (left and right), both lengths L. Please write a program that
#determines which cars should go to which lane, so that as many cars as possible fit on the ferry.
#Cars must enter in the order given in table A.

def ship(A,L):
    n,m=len(A),L
    F=[[[0 for k in range(m+1)] for j in range(m+1)] for i in range(n+1)]
    F[0][0][0]=1
    for i in range(1,n+1):
        x=A[i-1]
        if x>L:
            break
        for j in range(L+1):
            for k in range(L+1):
                if F[i-1][j][k]==1 and j+x<=L:
                    F[i][j+x][k]=1
                if F[i-1][j][k]==1 and k+x<=L:
                    F[i][j][k+x]=1

    c=0
    for i in range(n+1):
        for j in range(m+1):
            for k in range(m+1):
                if F[i][j][k]==1:
                    c=i

    if c==0:
        return "Tir blocked everyone );"
    def printsol(F,c,g,d):
        if c==0:
            return
        if F[c-1][g-A[c-1]][d]==1:
            printsol(F,c-1,g-A[c-1],d)
            print(c,"going up")
        else:
            printsol(F,c-1,g,d-A[c-1])
            print(c,"going down")

    for i in range(m+1):
        for j in range(m+1):
            if F[c][i][j]==1:
                printsol(F,c,i,j)
                return "The end"
