class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minPostion = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack)==1:
            self.minPostion.append(0)
        elif x < self.stack[self.minPostion[-1]]:
            self.minPostion.append(len(self.stack)-1)
        else:
            self.minPostion.append(self.minPostion[-1])
        return 

    def pop(self) -> None:
        self.stack.pop()
        self.minPostion.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.stack[self.minPostion[-1]]