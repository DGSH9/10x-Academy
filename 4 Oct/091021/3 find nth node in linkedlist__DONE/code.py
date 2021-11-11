# https://6793fdf6.widgets.sphere-engine.com/lp?hash=WfDahlylej
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
          
    def getNth(self, index):
        temp = self.head
        count = 1

        while(temp):
            if count ==index:
                return temp.data
                break
            temp = temp.next
            count+=1
        # return self.head
        return  
        ####WRITE CODE HERE###
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    index=int(input())
    print(linkedList.getNth(index))