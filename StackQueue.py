#cited from practical 3
import random
import numpy as np
class DSAStack:
    Default_Capacity = 100
    
    def __init__(self,max_capacity=Default_Capacity):
        self.stack = [None]* max_capacity
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.stack)
    
    def get_count(self):
        return self.count
    
    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.count-1]
    
    def push(self,value):
            if self.isFull():
                raise Exception("Stack Overflow")
            else:
                self.stack[self.count] = value
                self.count += 1
        
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Underflow")
        else:
            self.count -= 1
        return self.stack[self.count]
    
    def get(self,index):
        return self.stack[index]
    
    
class DSAQueue:
    DEFAULT_CAPACITY = 100

    def __init__(self, max_capacity=DEFAULT_CAPACITY):
        self.queue = [None] * max_capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == len(self.queue)

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue overflow")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) 
        if self.rear > 1:
            r = random.randint(self.front, self.rear - 1)
            self.queue[r], self.queue[self.rear - 1] = self.queue[self.rear - 1], self.queue[r]
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        value = self.queue[self.front]
        self.front = (self.front + 1) 
        self.count -= 1
        return value


    def front(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.front]
    def rear(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.queue[self.rear]

    def size(self):
        return self.count

