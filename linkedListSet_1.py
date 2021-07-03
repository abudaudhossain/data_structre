#Node class
class node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data #Assign data
        self.next = None # Initialize next as null

    # Linked list class contains a Node object
class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = node(1)
    second = node(2)
    third = node(3)

    llist.head.next = second
    second.next = third

    llist.printList()

