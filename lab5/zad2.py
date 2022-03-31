#Given is an array of n natural numbers A. Please give and pronoun-
#plement an algorithm that checks if it is possible to select a substring of numbers from A that add up to the given one
#values ​​of T.

def isSubsetSum(set,sum):
    n=len(set)
    subset = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])

    for i in range(n + 1):
        subset[i][0] = True

    for i in range(1, sum + 1):
        subset[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i - 1]:
                subset[i][j] = subset[i - 1][j] 
            if j >= set[i - 1]:
                subset[i][j] = (subset[i - 1][j] or
                                subset[i - 1][j - set[i - 1]])

    return subset[n][sum]
