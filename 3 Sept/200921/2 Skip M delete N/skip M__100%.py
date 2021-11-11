# Python program to delete M nodes after N nodes 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data, end=' ') 
            temp = temp.next
  
    def skipMdeleteN(self, M, N): 
        # Implment This
        temp = self.head
        while(temp):
            for _ in range(1, M):
                if temp is None:
                    return
                temp = temp.next
                     
            if temp is None :
                return
                
            temp2 = temp.next
            for _ in range(1, N+1):
                if temp2 is None:
                    break
                temp2 = temp2.next
            temp.next = temp2
            temp = temp2 

# Driver program to test above function 
n = int(input())
M,N = map(int, input().split())
llist = LinkedList() 
l = list(map(int, input().split()))
l.reverse()
for i in l:
    llist.push(i)

llist.skipMdeleteN(M, N) 
  
llist.printList()