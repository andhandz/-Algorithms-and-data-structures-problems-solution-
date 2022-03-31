#Please provide and implement an algorithm that finds the optimal value
#a small collection of objects in the discreet knapsack problem. The algorithm should run over time
#polynomial with the number of items and the sum of their perks.

def printsolution(F,W,P,i,w):#not necessery on this exercise
    if i==0:
        if w>=W[0]: return [0]
        return []
    if w>=W[i] and F[i][w]==F[i-1][w-W[i]]+P[i]:
        return printsolution(F,W,P,i-1,w-W[i])+[i]
    return printsolution(F,W,P,i-1,w)


def knapsack(W,P,MaxW):
    n=len(W)
    sum=0
    for i in range(n):
        sum+=P[i]

    F=[None]*n
    for i in range(n):
        F[i]=[0]*(sum)

    for i in range(n):
        for p in range(sum):
            if i>0 and F[i-1][p]!=0:
                if F[i][p]==0:
                    F[i][p]=F[i-1][p]
                else:
                    F[i][p]=min(F[i][p],F[i-1][p])
                if F[i][p+P[i]]==0:
                    F[i][p+P[i]]=F[i-1][p]+W[i]
                else:
                    F[i][p+P[i]]=min(F[i-1][p]+W[i],F[i][p+P[i]])
            if p+1==P[i]:
                if i==0 or F[i-1][p]==0:
                    F[i][p]=W[i]
                else: F[i][p]=min(F[i][p],W[i])

    pr=0
    for i in range(sum):
        if F[n-1][i]<MaxW and F[n-1][i]!=0:
            pr=i+1

    return pr
