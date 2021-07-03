class Node:
    def  __init__(self, value):
        self.next = None
        self.prev = None
        self.val = value

class DubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.size +=1
  

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                break
            node = node.next

        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
           

    def __str__(self):
            vals = []
            node = self.head
            while node is not None:
                vals.append(node.val)
                node = node.next
            return f"[{', '.join(str(val) for val in vals)}]"


my_list = DubleLinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(5)
my_list.remove(5)

print(my_list)
print(my_list.size)
