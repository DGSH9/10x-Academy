# https://6793fdf6.widgets.sphere-engine.com/lp?hash=9lKeDyuJJW
head = None
class Node:  
      
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data # Assign data  
        self.next =None
  
def segregateEvenOdd():
    global head
    temp1 = head
    ans_even = []
    ans_odd = []
    while(temp1 is not None):
        if(temp1.data %2==0):
            ans_even.append(temp1.data)
        else:
            ans_odd.append(temp1.data)
        temp1 = temp1.next
    ans_odd.sort()
    res = ans_even+ans_odd
    return res
  # Implement This only "BE CAREFUL HEAD IS GLOBALLY DECLARED"
          
# Given a reference (pointer to pointer) to the head 
# of a list and an int, push a new node on the front 
# of the list.  
def push(new_data): 
    global head 
  
    # 1 & 2: Allocate the Node & 
    #         Put in the data 
    new_node = Node(new_data) 
  
    # 3. Make next of new Node as head  
    new_node.next = head 
  
    # 4. Move the head to point to new Node  
    head = new_node 
  
# Utility function to print a linked list 
def printList(): 
    global head 
    temp = head 
    while(temp != None): 
          
        print(temp.data, end = " ") 
        temp = temp.next
          
    print(" ") 
  
# Driver program to test above functions  

n = int(input())
l = list(map(int, input().split()))
l.reverse()  
for i in l:
    push(i)  
segregateEvenOdd() 
printList()