def bubble_sort(list):
    k=len(list)
    for i in range(k-1):
        j=i
        while list[j]>list[j+1] and j>=0:
            list[j],list[j+1]=list[j+1],list[j]
            j-=1

    return list


#selection sort

def selection_sort(list):
    k=len(list)
    for i in range(k-1):
        j=i
        min=list[j]
        a=j
        while j<k:
            if list[j]<min:
                min=list[j]
                a=j
            j+=1
        list[i],list[a]=list[a],list[i]

    return list


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + "->" + str(self.next)


def tab_to_list(tab):
    head = Node("!")
    last = head
    for i in tab:
        last.next = Node(i, None)
        last = last.next
    return head


# zalozenie z wartownikiem
def insertionSort(head):
    nowa = Node("!")
    p = head.next
    while p != None:
        head.next = head.next.next
        cp, cp2 = nowa, nowa.next
        while cp2 != None and p.val > cp2.val:
            cp, cp2 = cp2, cp2.next
        cp.next = p
        p.next = cp2
        p = head.next
    return nowa


# tab = [0, 4, 2]
# print(tab)
# print(insertionSort(tab_to_lista(tab)))


def bubbleSort(head):
    if head == None:
        return None
    if head.next == None:
        return head
    marker = head
    while marker:
        marker = marker.next
        back = head.next
        front = head.next.next
        while front:
            if back.val > front.val:
                front.val, back.val = back.val, front.val
            back = back.next
            front = front.next
    return head

tab = [0, 4, 2]
print(tab)
print(tab_to_lista(tab))




