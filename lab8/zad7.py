# task7 A chessboard with dimensions n × n is given. Each field (i, j)
# has a cost (a number from the set {1,.., 5}) placed in array A (on field A [j] [i]). In the upper left corner
# of the board there is a king whose task is to go to the lower right corner, crossing the fields o
# minimum total cost. Please implement the kings path (A) function which computes a cost
# king's paths. This function should be as fast as possible.


#Idea: I interpret each field of the chessboard as a vertex, and also put x-1 vertices on the edge between the fields
#where x is the value of the vertex closer to the lower right corner, after creating such a graph, just release the algorithm
# shortest path from point a to b (problem 3)
