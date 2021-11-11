class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Counts the no . of occurrences of a node 
    # (search_for) in a linked list (head) 
    def count(self, search_for):
        temp = self.head
        if temp is None:
            return
        count1 = 0
        while(temp):
            if temp.data == search_for:
                count1+=1
                temp = temp.next
            else:
                temp = temp.next
        # print(count1)
        return count1

          
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
n = int(input())
l = list(map(int,input().split()))
for i in l:
    llist.push(i)
X = int(input())
print(llist.count(X))