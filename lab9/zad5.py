#The guide wants to transport a group of K tourists from
#town A to town B. However, there are many other towns on the way and buses run between the different towns
#different capacity. We have a given list of triples of the form (x, y, c), where x and y are the cities between which directly
#a bus with a capacity of c passengers runs.
#The handler must designate a common route for all tourists and must divide them into groups so
#so that each group can travel the route without dividing. Please enter some algorithm that calculates how much
#The guide has to divide the tourists (and which route they should follow) in the (fewest) groups, so that everyone
#they got from A to B.

def tour(G,A,B):
    inf = float('inf')
    n=0
    m=len(G)
    G.sort(key=lambda x: x[2], reverse=False)
    for i in range(m):
        n=max(n,G[i][0]+1,G[i][1]+1)
    d=[0 for i in range(n)]
    d[A]=inf
    for j in range(n):
        for i in range(m):
            d[G[i][1]]=max(d[G[i][1]],min(d[G[i][0]],G[i][2]))

    return d[B]
