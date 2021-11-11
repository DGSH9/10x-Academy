class Node:
    def __init__(self, key):
        self.data = key
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    @staticmethod
    def insert_node(val, current):
        temp = Node(val)
        current.next = temp
        current = current.next
        return current
    
    #complete the function given below
    @staticmethod
    def Negativity(List):
    	negCount = 0
    	total = 0
    	temp = List.head
    	while(temp != None ):
    		if temp.data < 0:
    			negCount+=1
    		total+=1
    		temp = temp.next
    		
    	return int((negCount/total)*100)


ll = LL()
num = [int(i) for i in input().split("->")]
ll.head = Node(num[0])
curr = ll.head
for i in num[1:]:
    curr = LL.insert_node(i, curr)
print(LL.Negativity(ll))