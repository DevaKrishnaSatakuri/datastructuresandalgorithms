#IMPLEMENTING USING A LIST
stack=[]
stack.append(22)
stack.append(33)
stack.append(44)

print(stack)
print(stack.pop())
print(stack)

#IMPLEMENTATION USING DEQUE
from collections import deque
stack=deque()
stack.append(25)
stack.append("Deva")
stack.append(45)
stack.append(55)

print("\r")
print(stack)
print(stack.pop())
print(stack)

#IMPLEMENTATION USING LIFOQUEUE
from queue import LifoQueue
stack=LifoQueue(maxsize=5)
stack.put(26)
stack.put(36)
stack.put(46)

print("\r")
print(stack.qsize())
print(stack.full())

stack.put(56)
stack.put(66)

print(stack.full())
print(stack.get())

#IMPLEMENTATION USING A LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

#PUSHING ELEMENTS
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node

#POPPING ELEMENTS
    def pop(self):
        if self.top is None:
            return "Stack underflow"
        popped=self.top.data
        self.top=self.top.next
        return popped

#PEEKING THE FIRST ELEMENT
    def peek(self):
        if self.top is None:
            return "Stack underflow"
        return self.top.data

#DISPLAYING ELEMENTS
    def display(self):
        temp=self.top
        if temp is None:
            return "Stack underflow"
        else:
            print("Stack (top->bottom) : ")
            while temp:
                print(temp.data)
                temp=temp.next

print("\r")
s=Stack()
s.push(22)
s.push(33)
s.push(44)
s.peek()
s.pop()
s.display()
