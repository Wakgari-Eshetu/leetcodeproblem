class MyCircularDeque:

    def __init__(self, k: int):
        self.que = [0] * k
        self.front = 0
        self.curr = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.que[self.front] = value
        self.curr += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        rear = (self.front + self.curr) % self.capacity
        self.que[rear] = value
        self.curr += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.capacity
        self.curr -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.curr -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        rear = (self.front + self.curr - 1) % self.capacity
        return self.que[rear]

    def isEmpty(self) -> bool:
        return self.curr == 0

    def isFull(self) -> bool:
        return self.curr == self.capacity