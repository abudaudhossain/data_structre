
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def printLinkList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next
        

if __name__ == '__main__':
    
    LinklistNum = list(map(int, input().split()))
  
    llist = Linklist()
    


    endnode = llist.head

    j = 0
    while j < len(LinklistNum):

        value = LinklistNum[j]
        temp = node(value)
        if(endnode):
            k = j+1
            valuek = LinklistNum[k]
            if(valuek == 1):
                endnode.next = temp
                endnode = temp
            else:
                temp.next = llist.head
                llist.head = temp

        else:
            llist.head = temp
            endnode = temp

        j = j + 2 
            


    llist.printLinkList()