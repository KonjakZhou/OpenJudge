# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root):
        if root == None:
            return root
        
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.mirrorTree(left)
        self.mirrorTree(right)
        return root