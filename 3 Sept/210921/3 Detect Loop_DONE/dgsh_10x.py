# Python program to detect loop in the linked list 

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

# Do not change anything above this line

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(fast_p is not None and slow_p is not None and fast_p.next is not None ):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if(slow_p == fast_p):
                return 1
        return 0     

        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
        # RETURN 1 IF LOOP IS THERE IN THE LINKED LIST, ELSE RETURN 0


# Do not change anything below this line
if __name__ == '__main__':
    
    n = int(input())

    # Start with the empty list 
    llist = LinkedList() 

    temp = [int(x) for x in input().split()]

    if(n<1):
        llist.head = None
    elif(n<2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next


    for i in range(2,n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    link = int(input())
    if(link!=-1):
        t = llist.head
        for _ in range(link-1):
            t = t.next
        curr.next = t

    # llist.printList()
    print(llist.detectLoop())