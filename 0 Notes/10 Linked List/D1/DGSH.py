class Node:
    def __init__(self, data = None, nextNode = None):
        self.data = data        #store int value
        self.nextNode = nextNode    #store Node Objects


node1 = Node(1, None) # 1 -> None
head  = node1
node2 = Node(2,None)     #2 -> None   #2-->is point to None
node3 = Node(3,None)     #3 -> None   #3-->is point to None 
node4 = Node(4,None)     #4 -> None   #4-->is point to None
node5 = Node(5,None)

node1.nextNode = node2  #1->2->None           #node1 is point to node2
node2.nextNode = node3  #1->2->3-->None       #node2 is point to node3
node3.nextNode = node4  #1->2->3->4->None     #node3 is point to node4


temp=head
while(temp != None):
    print(temp.data,end="->")
    temp=temp.nextNode