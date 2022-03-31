#Please implement a function that finds an element with the next key value
#than given in the BST

class BST_Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.parent=None

def find(root,key):
    while root!=None:
        if root.key==key:
            return root
        elif key<root.key:
            root=root.left
        else:
            root=root.right

    return None

def prev(root):
    if root == None:
        return None
    if root.left != None:
        root = root.left
        while root.right != None:
            root = root.right

        return root
    p = root.parent
    while p != None:
        if root != p.left:
            break
        root = p
        p = p.parent

    return p


def next(root):
    if root == None:
        return None
    if root.right!=None:
        root = root.right
        while root.left != None:
            root = root.left

        return root
    p=root.parent
    while p!=None:
        if root!=p.right:
            break
        root=p
        p=p.parent

    return p
