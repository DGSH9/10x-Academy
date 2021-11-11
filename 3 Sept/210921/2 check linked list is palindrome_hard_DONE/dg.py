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
          
    def isPalin(self):
        fast = self.head
        slow = self.head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        #check palindrome
        left = self.head
        right = prev
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        return True



        #####WRITE CODE HERE####
        

def read_list_input():
    vals = input().split(' ')
    linkedList = LinkedList() 
    for val in vals:
        linkedList.push(val)
    return linkedList

test_cases = int(input())
for i in range(test_cases):
    linkedList = read_list_input()
    print(linkedList.isPalin())