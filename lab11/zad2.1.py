#Consider the BST trees that additionally in each node
#le contain a field with the number of nodes in a given subtree. Please describe how to perform in such a tree
#the following operations:
#1.finding the i-go size of the item,
#2. determining which node in the tree is assigned to

class BST_m_Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None
        self.node_num=None

def i_element(root,i):
    if i>root.left.node_num+1:
        i-=(root.left.node_num+1)
        return i_element(root.right,i)

    elif i==root.left.node_num+1:
        return root

    else:
        return i_element(root.left,i)

def num_in_qu(root):
    v=root.key
    while root.left != None:
        root = root.left

    i=1
    while root.key!=v:
        root=next(root)
        i+=1

    return i

