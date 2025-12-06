class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Singlylinkedlist:
    def __init__(self):
        self.head= None
        self.size=0

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

    #TRAVESTING & PRINTING IN A SLL
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next
        print("None")

    # SIZE OF THE SLL
    def size(self):
        current=self.head
        count=0
        while current is not None:
            count=count+1
            current=current.next
        return count
    #OPTIMIZED WAY TO GET SIZE
    def get_size(self):
        return self.size


sll=Singlylinkedlist()
sll.build_list()
sll.print_list()
print("Len =",sll.get_size())


