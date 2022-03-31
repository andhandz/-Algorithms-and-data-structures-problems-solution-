#We have a given table with the denominations of coins used in certain
#country, and the amount of T. Please enter some algorithm that calculates the minimum amount of coins needed to spend
#T amounts (the greedy algorithm that spends the largest coin first, does not work: for coins 1, 5, 8 it will spend
#amount 15 as 8 + 5 + 1 + 1 instead of 5 + 5 + 5).

def mincoins(coins,val):
    n = len(coins)

    t = [100 for _ in range(val+1)]

    t[0] = 0

    for i in range(1,val+1):
        for j in range(n):

            if coins[j] <= i:
                rest = t[i-coins[j]]

                if rest < 100 and rest + 1 < t[i]:
                    t[i] = rest + 1
    return t[len(t)-1]
