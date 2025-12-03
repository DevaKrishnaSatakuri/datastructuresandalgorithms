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
sll=Singlylinkedlist()
sll.build_list()
print(sll.head.data )


