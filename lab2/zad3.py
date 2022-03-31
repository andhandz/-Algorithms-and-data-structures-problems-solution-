#The sorted array A [1 ... n] and the number x are given. Please write pro
#a gram that states if there are indices i and j such that A [i] + A [j] = x.

def exist(t,x):
    a=0
    b=len(t)-1
    for i in range(len(t)-1):
        sum = t[a] + t[b]
        if sum==x:
            return True
        elif sum>x:
            b-=1
        else:
            a+=1

    return False
