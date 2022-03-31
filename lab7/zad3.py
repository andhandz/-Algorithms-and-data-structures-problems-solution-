#We have a trailer with a capacity of K kilograms and a collection of loads
#with weights in 1,. . . , in n. The weight of each charge is a power of two (that is, for example, for seven charges
#weights can be 2, 2, 4, 8, 1, 8, 16, and the capacity of the trailer K = 27). Please enter some greedy algorithm (i
#justify its correctness), which selects the loads so that the trailer is as full as possible
#(but without exceeding the capacity) and at the same time we used as few loads as possible. (But if it can
#eg fully load a trailer with 100 loads, or load up to K - 1 using
#one load, the first solution is better).

def loading(A,k):
    n = len(A)
    A.sort()
    cnt = 0 
    idx = n - 1

    while k > 0 and idx >= 0:
        if k >= A[idx]:
            cnt += 1
            k -= A[idx]
        idx -= 1

    return 
