class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Singlylinkedlist:
    def __init__(self):
        self.head= None
        self.size=0

#NAIVE METHOD
  #  def build_list(self):
  #     first=Node(10)
  #     second=Node(20)
  #     third=Node(30)
  #     fourth=Node(40)

  #     first.next=second
  #     second.next=third
  #     third.next=fourth

  #     self.head=first

    #TRAVESTING & PRINTING IN A SLL
    def print_list(self):
        current=self.head
        while current is not None:
            print(current.data,end="-->")
            current=current.next
        print("None")

    # SIZE OF THE SLL
#    def size(self):
#       current=self.head
#        count=0
#        while current is not None:
#            count=count+1
#            current=current.next
#        return count

    #OPTIMIZED WAY TO GET SIZE
    def get_size(self):
        return self.size

    #INSERTING AT THE BEGINNING
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    #INSERTING AT THE END
    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
        self.size+=1

    # INSERTING AT ANY POSITION
    def inset_at_position(self,data,position):
        if position<0:
            return ValueError("Invalid position : cannot be negative")
        if position>self.size:
            return ValueError("Invalid position : cannot be higher than size")
        new_node=Node(data)
        if position == 0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            counter=0
            while counter<position-1:
                counter+=1
                current=current.next
            new_node.next=current.next
            current.next=new_node
        self.size+=1


sll=Singlylinkedlist()
sll.insert_at_beginning(11)
sll.insert_at_beginning(12)
sll.insert_at_beginning(-13)
sll.insert_at_end(21)
sll.insert_at_end(23)
sll.inset_at_position(33,3)
sll.print_list()
print("Len =",sll.get_size())


