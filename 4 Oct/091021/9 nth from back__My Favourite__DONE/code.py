# https://6793fdf6.widgets.sphere-engine.com/lp?hash=imiC2IAM73

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
 
 
def length_llist(llist):
    length = 0
    current = llist.head
    while current:
        current = current.next
        length = length + 1
    return length
 
 
def return_n_from_last(llist, n):
   #Implement this
    temp = llist.head
    total_count = 0
    while(temp is not None):
       total_count+=1
       temp = temp.next

    From_begining =  ((total_count - n) +1)
    temp2 = llist.head
    count = 1

    while(temp2 is not None):
        if count == From_begining:
            return temp2.data
            break
        temp2 = temp2.next
        count+=1
 

N, n = map(int, input().split(' ')) 
a_llist = LinkedList()

l = list(map(int, input().split(' ')))
for i in l:
    a_llist.append(i) 

value = return_n_from_last(a_llist, n)
 
print(value)