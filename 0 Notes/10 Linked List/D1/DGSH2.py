class Node:
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next
    
    #create 
    #insert at head
    #insert at tail
    #insert at b/w
    #display
    #delete
class SinglyLinkedList():
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def display(self):
        temp = self.head
        while(temp !=None):
            print(temp.val,end="->")
            temp = temp.next


    def insertATHead(self,value):
        #create a new node
        #point new node to head
        #change the head to new node
        newNode = Node(value)
        if self.head is None:       #if head is empty
            self.head = newNode
            return
        newNode.next = self.head    #if head is not empty
        self.head = newNode

    def inserAtEnd(self,valu1):
        #create new node
        #traverse to the new node if we have tail then point the tail
        #............
        #without tail
        newNode = Node(valu1)
        temp = self.head
        while(temp.next !=None):
            temp=temp.next
        temp.next = newNode

linkedList = SinglyLinkedList()

linkedList.insertATHead(1)
linkedList.insertATHead(2)
linkedList.insertATHead(3)
linkedList.insertATHead(4)
linkedList.display()

print("\n")
linkedList.inserAtEnd(8)
linkedList.inserAtEnd(9)
linkedList.display()
    

































# node1 = Node(1,None)
# head = node1
# node2 = Node(2,None)
# node3 = Node(3,None)
# node4 = Node(4,None)

# node1.nextNode = node2
# node2.nextNode = node3
# node3.nextNode = node4

# temp=head
# while(temp != None):
#     print(temp.data,end="->")
#     temp = temp.nextNode