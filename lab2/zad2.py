#Please implement an algorithm that counts the number of inversions in an array. (Inversion is a pair of indices i, j such,
#that i <j and T [i]> T [j])

r=0
def merge(T1,T2):
    global r
    T=[]
    n=len(T1)+len(T2)
    for i in range(n):
        if len(T1)==0:
            T.append(T2[0])
            T2=T2[1:]
        elif len(T2)==0 or T1[0]<=T2[0]:
            T.append(T1[0])
            T1=T1[1:]
        else:
            r+=len(T1)
            T.append(T2[0])
            T2=T2[1:]

    return T

def merge_sort(T):
    global r
    n=len(T)
    if n>1:
        L=merge_sort(T[:(n//2)])
        P=merge_sort(T[(n//2):])

        T=merge(L,P)

    return T

def count_inversion(T):
    global r
    print(merge_sort(T))
    return r
