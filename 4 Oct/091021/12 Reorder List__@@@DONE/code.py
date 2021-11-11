# https://6793fdf6.widgets.sphere-engine.com/lp?hash=ZixaUQyq1u

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

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

# Do not change anything above this line

    def reorderList(self):
        # reverse linked list
        def revrseLL(head1):
            temp = head1
            prev = None
            while(temp):
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
            return prev

        # count total element in linked list
        E1 = self.head
        l = 0
        while(E1):
            l += 1
            E1 = E1.next

        # finding mid
        mid = self.head
        for _ in range(l//2):
            mid = mid.next

        # element after mid
        E2 = revrseLL(mid.next)  # using reverse function
        mid.next = None

        E1 = self.head
        while(E2):
            nextE1 = E1.next
            E1.next = E2

            nextE2 = E2.next
            E2.next = nextE1

            # increament E1 and E2
            E1 = nextE1
            E2 = nextE2

        return self.head

        # YOU ONLY NEED TO COMPLETE THIS FUNCTION.
# Do not change anything below this line
if __name__ == '__main__':

    n = int(input())

    # Start with the empty list
    llist = LinkedList()

    temp = [int(x) for x in input().split()]

    if(n < 1):
        llist.head = None
    elif(n < 2):
        llist.head = Node(temp[0])
    else:
        llist.head = Node(temp[0])
        second = Node(temp[1])
        llist.head.next = second
        curr = llist.head.next

    for i in range(2, n):
        t = Node(temp[i])
        curr.next = t
        curr = curr.next

    llist.head = llist.reorderList()
    llist.printList()
