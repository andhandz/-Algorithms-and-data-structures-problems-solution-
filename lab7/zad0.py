#The tank goes from point A to point B. Burning the tank is
#exactly one liter of fuel for one kilometer of the route. The tank holds exactly 1 liters of fuel. Route from A
#do B is the line with gas stations (in positions that are natural numbers; A
#is at position 0). Please provide the algorithms for the following cases:
#(a) We designate the stations where we refuel so that the total number of refueling is minimal.
#(b) We designate the stations so that the cost of travel is minimal (in this case, each station has an additional
#the price per liter of fuel). We can refuel any amount of fuel at each station.
#(c) as above, but if we refuel at the station, we must refuel to the full.

#a
def tank1(S,L,t):
    c=0
    b=L
    n=len(S)
    for i in range(n):
       k=t
       if i!=n-1:
          k=S[i+1]
       if i==0:
           b-=S[i]
       else:
          b-=(S[i]-S[i-1])
       if b<0:
           return -1
       if k-S[i]>b:
           c+=1
           b=L
       if t-S[i]<=b:
        return c

    if t-S[n-1]>L:
        return -1


# S=[3,7,11,13,17,19,23]
# print(tank1(S,6,29))

#b
S=[(3,2),(7,3),(11,2.5),(13,4),(17,2),(19,1.7),(23,3)]

#at the beginning, we check all the stations to which we can reach and choose the cheapest one,
# from it we check all the stations to which we will be able to reach by refueling,
# if all stations are more expensive, we refuel to the full and get to the cheapest of them,
#if one is cheaper, we refuel enough to get to it, after reaching it we repeat the algorithm

def tank2(S,L,t):
    n=len(S)
    i=0
    min=100
    ind=0
    c=0
    while S[i][0]<=L:
        if S[i][1]<min:
            min=S[i][1]
            ind=i
        i+=1
    i=ind
    b=L
    b-=S[i][0]
    while i<n-1:
        if i==n-2:
            if S[i][1]>=S[i+1][1]:
                c+=S[i][1]*(S[i+1][0]-S[i][0]-b)
                c+=S[i+1][1]*(t-S[i+1][0])
            else:
                if t-S[i][0]>L:
                    c+=(L-b)*S[i][1]
                    b=L-(S[i+1][0]-S[i][0])
                    c+=S[i+1][1]*(t-S[i+1][0]-b)
                else:
                    c+=S[i][1]*(t-S[i][0]-b)
            return c
        a=0
        j=i+1
        min=100
        while j<n-1 and S[j][0]-S[i][0]<=L:
            if S[j][1]<S[i][1]:
                ind=j
                if b<S[j][0]-S[i][0]:
                    a=0
                    c+=(S[j][0]-S[i][0]-b)*S[i][1]
                    b=S[j][0]-S[i][0]
                break
            if S[j][1]<min:
                a = 1
                ind=j
                min=S[j][1]
            j+=1
        if a==1:
            if S[i][0]+L<=t:
                c+=S[i][1]*(L-b)
                b=L
            else:
                c+=S[i][1]*(t-S[i][0])
                return c
        b-=(S[ind][0]-S[i][0])
        i=ind

    c += S[n-1][1] * (t - S[n-1][0] - b)
    return c

#print(tank2(S,10,28))
#c
#f(i,b)- min cost to i-station wth b gas
#f(i,b)=min(f(j,b)+P(j)*(L-b)) for each j, that S(i)-S(j)<=L
def tank3(S,L,t):
    n=len(S)
    F=[[1000,10] for i in range(n+1)]
    k=0
    while S[k][0]<=L:
        F[k][0]=0
        F[k][1]-=S[k][0]
        k+=1

    if k==0:
        return -1
    S.append([t,False])
    for i in range(k,n+1):
        if S[i][0]-S[i-1][0]>L:
            return -1
        j=i-1
        while j>=0 and S[i][0]-S[j][0]<=L:
            F[i][0]=min(F[i][0],F[j][0]+S[j][1]*(L-F[j][1]))
            if F[i][0]==F[j][0]+S[j][1]*(L-F[j][1]):
                F[i][1]=L-(S[i][0]-S[j][0])
            j-=1

    return F[n][0]
