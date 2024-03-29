# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        n = len(nestedList)
        self.stack = [nestedList[i] for i in range(n-1, -1, -1)]
    
    def next(self) -> int:
        return self.stack.pop()
    
    def hasNext(self) -> bool:
        while True:
            if len(self.stack)>0:
                if self.stack[-1].isInteger():
                    return True

                cur = self.stack.pop()
                res = cur.getList()
                n = len(res)
                if n > 0:
                    self.stack.extend([res[i] for i in range(n-1, -1, -1)])
            else:
                return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())