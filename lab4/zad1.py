#Please propose an algorithm that sorts the array A with n numbers in linear time
#from the set 0,. . . , n 2 - 1.

from random import randint, seed
def count(x):
    a=0
    while x>=1:
        a+=1
        x//=10

    return a

def radixsort(T,n):
    a=count((n**2)-1)
    for i in range(a):
        k=0
        T1=T.copy()
        for j in range(10):
            for l in range(n):
                if (T1[l]//10**i)%10==j:
                    T[k]=T1[l]
                    k+=1

    return T
