#Please propose an algorithm that sorts a sequence of words of different lengths in time proportional to
#the sum of the lengths of these words.

def rsort(Al,max):
    alp = "abcdefghijklmnopqrstuwxyz"
    Ac = Al.copy()
    k = 0
    for i in range(len(alp)):
        for j in range(len(Al)):
            if Ac[j][max - 1] == alp[i]:
                Al[k] = Ac[j]
                k += 1

    return Al

def strsort(A):
    max = 0
    for i in range(len(A)):
        if len(A[i]) > max:
            max = len(A[i])

    Al=[[]for i in range(max)]

    for i in range(len(A)):
        Al[len(A[i])-1].append(A[i])

    A1=[]
    for i in range(max):
        for j in range(len(Al[max-1])):
            A1.append(Al[max - 1][j])

        A1=rsort(A1,max)
        max-=1

    A=A1
    return A
