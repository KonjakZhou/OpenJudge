# base version
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s2.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        return 

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            return self.s1[-1]
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s1:
            return False
        return True

# advanced version
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = list()
        self.s2 = list()
        self.state = 1

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.state == 1:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.state =2
        self.s2.append(x)
        return 

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.state == 2:
            while self.s2:
                self.s1.append(self.s2.pop())
            self.state = 1
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.empty():
            if self.state == 2:
                while self.s2:
                    self.s1.append(self.s2.pop())
                self.state = 1
            return self.s1[-1]
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.s1 or self.s2:
            return False
        return True