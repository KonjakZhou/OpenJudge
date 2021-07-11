# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        def getRoot(preorder, inorder):
            n = len(preorder)
            if n==0:
                return None
            if n==1:
                return TreeNode(preorder[0])
            
            node = TreeNode(preorder[0])
    
            for i in range(n):
                if inorder[i] == node.val:
                    node.left = getRoot(preorder[1:1+i], inorder[0:i])
                    node.right = getRoot(preorder[i+1:], inorder[i+1:])
                    return node
        
        return getRoot(preorder, inorder)
                    