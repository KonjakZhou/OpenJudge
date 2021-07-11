class CQueue:

    def __init__(self):
        self._stack_out = list()
        self._stack_in = list()

    def appendTail(self, value):
        self._stack_in.append(value)

    def deleteHead(self):
        if len(self._stack_out) == 0:
            while len(self._stack_in) > 0:
                self._stack_out.append(self._stack_in.pop())
        if len(self._stack_out) == 0:
            return -1
        return self._stack_out.pop()