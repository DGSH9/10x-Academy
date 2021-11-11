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
    temp = llist.head
    count = 0
    while(temp is not None):
        temp = temp.next
        count+=1
    # print("check--->",count)
    ans = count - n
    # print("check--->",ans)   # 1
    temp1 = llist.head
    count1 = 0
    while(count1 < ans and temp1 is not None):
        temp1 = temp1.next
        count1+=1
    return temp1.data
    

   #Implement this
 

N, n = map(int, input().split(' ')) 
a_llist = LinkedList()

l = list(map(int, input().split(' ')))
for i in l:
    a_llist.append(i) 

value = return_n_from_last(a_llist, n)
 
print(value)