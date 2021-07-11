# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def judge(wow, reverse):
            if wow == None and reverse == None:
                return True
            if wow == None or reverse == None:
                return False
            if wow.val != reverse.val:
                return False
            return judge(wow.left, reverse.right) and judge(wow.right, reverse.left)
        
        return judge(root, root)