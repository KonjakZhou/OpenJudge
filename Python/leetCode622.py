class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = list(range(k))
        self.len = k
        self.state = -1
        self.h = 0
        self.t = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.queue[self.t] = value

        self.t = (self.t + 1) % self.len
        if self.t == self.h:
            self.state = 1
        else:
            self.state = 0
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.h = (self.h + 1) % self.len

        if self.h == self.t:
            self.state = -1
        else:
            self.state = 0
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.h]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.t + self.len - 1) % self.len]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.state == -1:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.state == 1:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1))
print(circularQueue.enQueue(2))
print(circularQueue.enQueue(3))
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.enQueue(4))
print(circularQueue.Rear())