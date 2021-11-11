class Node: 
    def __init__(self, value): 
        self.data = value 
        self.next = None
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_value): 
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        
#1 0 2 1 3 0
    def makeListAndPrint(self):
        hd = None
        tl = None
        temp=self.head
        while temp is not None:
            if hd is None:
                hd=Node(temp.data)
                tl=hd
            else:
                if(temp.next.data=='0'):
                    tmp=Node(temp.data)
                    tmp.next=hd
                    hd=tmp
                else:
                    tmp=Node(temp.data)
                    tl.next=tmp
                    tl=tl.next
            temp=temp.next.next
        temp=hd
        # print("________________")
        while temp is not None:
            print(temp.data)
            temp=temp.next

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    linkedList.makeListAndPrint()