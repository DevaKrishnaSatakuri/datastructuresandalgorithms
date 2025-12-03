class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Singlylinkedlist:
    def __init__(self):
        self.head= None
#NAIVE METHOD
    def build_list(self):
        first=Node(10)
        second=Node(20)
        third=Node(30)
        fourth=Node(40)

        first.next=second
        second.next=third
        third.next=fourth

        self.head=first
    #TRAVESTING LL
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next
        print("None")
sll=Singlylinkedlist()
sll.build_list()
sll.print_list()
print(sll.head.data)


