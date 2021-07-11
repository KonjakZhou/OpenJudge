# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isSub(A, B):
            if B==None:
                return True
            if A==None:
                return False
            
            if A.val == B.val:
                return isSub(A.left, B.left) and isSub(A.right, B.right)

            return False
        
        if B==None or A==None:
            return False
        if isSub(A,B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

