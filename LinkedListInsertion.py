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
            # print(temp.data)
            temp = temp.next
        

if __name__ == '__main__':
    
    LinklistNum = list(map(int, input().split()))
    print(LinklistNum)
    # print(LinklistNum[2])

    llist = Linklist()
    
    
    # tempnode = None
    # for i in LinklistNum:
    #     if(tempnode):
    #         tempnode = node(i)
    #         templinknode.next = tempnode
    #         templinknode = tempnode
    #     else:
    #         llist.head = node(i)
    #         tempnode = llist.head
    #         templinknode = llist.head
        

    endnode = llist.head

    j = 0
    while j < len(LinklistNum):
        # print(j)
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
            



       
        


    # _1st = node(9)
    # _2nd = node(5)
    # _3th = node(6)
    # _4th = node(2)
    # _5th = node(5)

    # llist.head = _5th
    # llist.head.next = _4th
    # _4th.next = _1st
    # _1st.next = _2nd
    # _2nd.next = _3th

    llist.printLinkList()



    
