# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root, x, y):
        def dfs(root, aim, depth, father):
            if root.val==aim:
                return depth, father
            
            if root.left!=None:
                d, f = dfs(root.left, aim, depth+1, root)
                if d != None:
                    return d,f
            if root.right!=None:
                d, f = dfs(root.right, aim, depth+1, root)
                if d!=None:
                    return d,f
            return None, None

        dx, fx = dfs(root, x, 0, None)
        dy, fy = dfs(root, y, 0, None)
        if dx==dy and fx!=fy:
            return True
        return False