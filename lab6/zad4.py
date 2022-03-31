#A frog is jumping on the number line. It has to get from zero to n - 1 by jumping
#exclusively towards larger numbers. The jump from i to j (j> i) costs it j - i units of energy, a
#its energy can never fall below zero. At first, the frog has 0 energy, but luckily it has no energy
#some numbers — including zero — include snacks with a certain energy value (snack value
#adds to Zbigniew's current energy). Please propose an algorithm that computes the minimum number
#jumps needed to get from 0 to n - 1 have a given table A with the energy values ​​of snacks on
#each of the numbers.

import math
def frogson_ziomal(A):
    n=len(A)
    inf=float('inf')
    F=[[inf for j in range(n)] for i in range(n)]
    if A[0]>=n:
        return 1
    F[0][A[0]]=0

    for i in range(1,n):
        for j in range(0,i):
            for k in range(i-j,n):
                y=k+A[i]-(i-j)
                if y<n:
                    F[i][y]=min(F[i][y],F[j][k]+1)

    m=inf
    for i in range(n):
        m=min(m,F[n-1][i])
    if m==inf:
        m=-1
    return m
