# #QUEUE
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#
#     def is_empty(self):
#         return self.front is None
#
# #ADDING ELEMENTS TO A QUEUE
#     def enqueue(self,data):
#         new_node=Node(data)
#
#         if self.rear is None:
#             self.front=self.rear=new_node
#             return
#         self.rear.next=new_node
#         self.rear=new_node
#
# #DELETING ELEMENTS FROM A QUEUE
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         self.front=self.front.next
#         return self.front.data
#         #(Not good with complexity)
#         # temp=self.front
#         # temp.next=self.front
#         #
#         # if self.front is None:
#         #     self.rear=None
#         # return temp.data
#
#     def display(self):
#         temp=self.front
#         print("Queue elements (front-->rear) : ")
#         while temp is not None:
#             print(temp.data, end="-")
#             temp=temp.next
#
#
#
# q=Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.dequeue()
# print(q.front.data)
# q.display()
# q.dequeue()
# print("\r")
# q.display()
# print("\r")
# print(q.rear.data)

#CIRCULAR QUEUE
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class CircularQueue:
    def __init__(self):
        self.rear=None

    def is_empty(self):
        return self.rear is None

#ADDING ELEMENTS IN A QUEUE
    def enqueue(self, data):
        new_node=Node(data)

        if self.rear is None:
            self.rear=new_node
            self.rear.next=self.rear
        else:
            new_node.next=self.rear.next
            self.rear.next=new_node
            self.rear=new_node


#REMOVING ELEMENTS
    def dequeue(self):
       if self.is_empty():
           return None

       if self.rear == self.rear.next:
           self.rear=None
       else:
           self.rear.next= self.rear.next.next


    def peek(self):
        if self.is_empty():
            return None
        print(self.rear.next.data)
        return None

    #PRINTING ELEMENTS
    def display(self):
        if self.is_empty():
            return None
        temp=self.rear.next
        print("\r")
        print("Circular Queue : ", end=" ")
        while True:
            print(temp.data, end=" ")
            temp=temp.next
            if temp==self.rear.next:
                break
        print()


cq=CircularQueue()
cq.enqueue(22)
cq.enqueue(33)
cq.enqueue(44)
cq.enqueue(55)
cq.enqueue(66)
cq.enqueue(77)
cq.dequeue()
cq.peek()
cq.display()
