#Given is a graph G = (V, E) whose vertices represent points
#navigation over Byteotia, and the edges represent the air corridors between these points. Every
#air corridor ei ∈ E is related to the optimum flight altitude pi ∈ N (expressed in meters).
#The regulations allow for a flight along a given corridor if the altitude of the plane differs from the optimal one at most by t
#meters. Please propose an algorithm (without implementation) that checks if there is a possibility of overflying
#from a given point x ∈ V to a given point y ∈ V in such a way that the plane never changes its altitude.
#The algorithm should be correct and as fast as possible. Please estimate its time complexity.


#Idea: I pass dfs saving the smallest and greatest value in the transition (and points visited), each time I can pass
#only on the edge after which the transition, the difference between min and max will still be no more than 2t, if I can't go anywhere,
#then I go back to the point until it is possible to go to the given edge, if there is no longer an edge on which I can pass
#then I check if the destination has been visited.
