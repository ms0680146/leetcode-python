# Circular Queue
# functions: enqueue, dequeue, isFull, isEmpty

class CircularQueue:
    def __init__(self, maxSize):
        self.queue = [None] * maxSize
        self.maxSize = maxSize
        self.head = -1
        self.tail = -1

    def isFull(self): # head = tail + 1
        return self.head == (self.tail + 1) % self.maxSize
    
    def isEmpty(self):
        return self.head == -1
    
    def enqueue(self, data):
        if self.isFull():
            print("The circular queue is full\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
            return True
        else:
            self.tail = (self.tail + 1) % self.maxSize
            self.queue[self.tail] = data
            return True
        
    def dequeue(self):
        if self.isEmpty():
            print("The circular queue is empty\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.maxSize
            return temp
        
        
q = CircularQueue(5)
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(40))
print(q.enqueue(50))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.queue)
print(q.head)
print(q.tail)