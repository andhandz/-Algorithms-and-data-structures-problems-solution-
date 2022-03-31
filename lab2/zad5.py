#We have an array A with n numbers. Please propose an algorithm with complexity
#O (n), which states whether there is a number x (the so-called leader of A) that appears in more than half of the position in A.

def candidate(t):
    count=1
    maj=0
    for i in range(len(t)):
        if t[i]==t[maj]:
            count+=1
        else:
            count-=1
        if count==0:
            maj=i
            count=1

    return t[maj]

def leader(t):
    a=candidate(t)
    count=0
    for i in range(len(t)):
        if t[i]==a:
            count+=1
        if count>len(t)/2:
            return True

    return False
