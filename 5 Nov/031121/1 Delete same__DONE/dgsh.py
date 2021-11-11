class Node:  
  
    # Constructor to initialize  
    # the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None
  
class LinkedList:  
  
    # Function to initialize head  
    def __init__(self):  
        self.head = None
  
    # Function to insert a new node  
    # at the beginning  
    def push(self, new_data):  
        new_node = Node(new_data)  
        new_node.next = self.head  
        self.head = new_node  
  
    
    
  
    # Utility function to print the  
    # linked LinkedList  
    def printList(self):  
        temp = self.head  
        while(temp):  
            print(temp.data , end = ' ') 
            temp = temp.next
        print('')
      
    # This function removes duplicates  
    # from a sorted list          
    def removeDuplicates(self):
        ans = set()
        temp = self.head
        if temp is None:
            return
        
        ans.add(temp.data)
        while(temp.next is not None):
            if temp.next.data in ans:
                temp.next = temp.next.next
            else:
                ans.add(temp.next.data)
                temp = temp.next
        return
        #Implement this only
         
  
# Driver Code  
testCase = int(input())
for _ in range(testCase):
	listSize = int(input())
	givenElements = list(map(int, input().split()))
	givenElements.reverse()
	llist = LinkedList()
	for element in givenElements:
		llist.push(element)
	llist.removeDuplicates()
	llist.printList()