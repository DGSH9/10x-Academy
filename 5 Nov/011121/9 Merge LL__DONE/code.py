# https://6793fdf6.widgets.sphere-engine.com/lp?hash=BmNu9LQhHx

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


def reverse_llist(llist):
    before = None
    current = llist.head
    if current is None:
        return
    after = current.next
    while after:
        current.next = before
        before = current
        current = after
        after = after.next
    current.next = before
    llist.head = current


def mergeLists(headA, headB):
    res = None
    if headA.data < headB.data:
        head = Node(headA.data)
        res = head
        headA = headA.next
    else:
        head = Node(headB.data)
        res = head
        headB = headB.next

    while (headA is not None and headB is not None):
        if headA.data < headB.data:
            res.next = Node(headA.data)
            res = res.next
            headA = headA.next
        else:
            res.next = Node(headB.data)
            res = res.next
            headB = headB.next

    while(headA is not None):
        res.next = Node(headA.data)
        res = res.next
        headA = headA.next

    while(headB is not None):
        res.next = Node(headB.data)
        res = res.next
        headB = headB.next
    return head


# Create 2 lists
listA = LinkedList()
listB = LinkedList()

# Add elements to the list in sorted order
n1 = int(input())
l1 = list(map(int, input().split(' ')))
n2 = int(input())
l2 = list(map(int, input().split(' ')))
for i in l1:
    listA.append(i)
for i in l2:
    listB.append(i)
# Call the merge function
listA.head = mergeLists(listA.head, listB.head)

# Display merged list
listA.display()
