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
            print(current.data, end = ' ')
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
    set1 = []
    temp1 = headA
    if temp1 is None:
        return
    
    set1.append(temp1.data)
    while(temp1.next is not None):
        set1.append(temp1.next.data)
        temp1 = temp1.next
    # print(set1)
    # set2 = set()
    temp2 = headB
    if temp2 is None:
        return
    
    set1.append(temp2.data)
    while(temp2.next is not None):
        set1.append(temp2.next.data)
        temp2 = temp2.next
    # print(set1)
    set1.sort()
    for i in set1:
        print(i,end=" ")
    
    

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