#Implementation of the MergeSort algorithm for sorting lists


class Node:

    def __init__(self,val=None, next=None):
        self.next=next
        self.val=val

    def __str__(self):
        return str(self.val) + "->" + str(self.next)

def tab_to_lista(tab):
    head = Node("!")
    last = head
    for i in tab:
        last.next = Node(i, None)
        last = last.next
    return head


def merge(first1,first2):
    n1=first1.next
    n2=first2.next
    first=Node("!")
    n = first
    while n1!=None and n2!=None:
        if n1.val<n2.val:
            n.next=n1
            n1=n1.next
        else:
            n.next=n2
            n2=n2.next
        n=n.next

    while n2!=None:
        n.next=n2
        n2=n2.next
        n=n.next

    while n1!=None:
        n.next=n1
        n=n.next
        n1=n1.next

    return first

def count(first):
    p=first
    i=0
    while p.next!=None:
       i+=1
       p=p.next

    return i

def mergesort(first):
    n=count(first)
    if n>1:
        l=first
        for i in range(n//2):
            l=l.next
        p=Node("!")
        p.next=l.next
        l.next=None
        L=mergesort(first)
        P=mergesort(p)
        first=merge(L,P)
    return first

tab = [0, 4, 2,7,3,11,12,10,15,3,6,4,8]
print(tab)
print(mergesort(tab_to_lista(tab)))
