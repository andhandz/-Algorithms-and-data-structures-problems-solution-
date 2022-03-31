#Please propose an algorithm that, given two words A and B of length n, each over
#with the alphabet of length k, checks if A and B are anagrams of each other.

def anagrams(str1,str2,k):
    if len(str1)!=len(str2):
        return False
    Val=[0]*k
    for i in range(len(str1)):
        if Val[ord(str1[i])]==0:
            Val[ord(str1[i])]=ord(str1[i])
        else:
            Val[ord(str1[i])]+=1

    for i in range(len(str2)):
        Val[ord(str2[i])]-=1

    for i in range(len(str1)):
        if Val[ord(str1[i])]+1!=ord(str1[i]):
            return False

    return True
