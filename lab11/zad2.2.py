#Please suggest an algorithm that computes the sum of all values ​​in a binary tree
#defined on nodes of the type:
#class BNode:
#def __init __ (
#self.left
#self.right
#self.parent
#self.value
#self, value):
#= None
#= None
#= None
#= val
#The program can only use a fixed number of variables (but it is allowed to change the tree structure, see
#on condition that the tree will be restored to its initial state after the computation is completed.)

def BST_sum(root):
    while root.left!=None:
        root=root.left

    sum=0
    while root!=None:
        sum+=root.key
        root=next(root)

    return sum

from queue import Queue
