#Given is a chessboard A with dimensions n × n. A chessboard
#contains rational numbers. It is necessary to move from field (1, 1) to field (n, n) using only "down" moves
#and "right". Entering a given field costs as much as the number there. Please enter some algorithm
#finding a route with the minimum cost.

def min_cost(T):
    N = len(T)
    F = [[0] * N for _ in range(N)]
    F[0][0] = T[0][0]

    for i in range(1, N):
        F[i][0] = A[i][0] + F[i - 1][0]

    for i in range(1, N):
        F[0][i] = A[0][i] + F[0][i - 1]

    for i in range(1, N):
        for j in range(1, N):
            F[i][j] = min(F[i - 1][j], F[i][j - 1]) + A[i][j]

    return F[N - 1][N - 1]
