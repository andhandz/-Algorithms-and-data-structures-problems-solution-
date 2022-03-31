#Please propose / implement a merging algorithm for k sorted arrays with a total length of n
# into one sorted array at O ​​(n ∗ log (k)) time.
def merge(T1,T2):
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
            T.append(T2[0])
            T2=T2[1:]

    return T

def merge_sort(T):
    n=len(T)
    if n>1:
        L=merge_sort(T[:(n//2)])
        P=merge_sort(T[(n//2):])

        T=merge(L,P)

    return T

def one_tab(T,k):
    tab=[]
    for i in range(k):
        tab+=T[i]

    return tab

def sorted_tab(T,k):
    t=one_tab(T,k)
    tab=merge_sort(t)
    return tab
