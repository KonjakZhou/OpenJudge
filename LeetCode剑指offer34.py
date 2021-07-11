# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, target: int):
        def dfs(root, path, target, ans, sumPath):
            curSum = root.val + sumPath
            if curSum == target:
                ans.append(path[:])
                return 
            if curSum > target:
                return 
            
            path.append(root.val)
            sumPath += root.val
            if root.left!=None:
                dfs(root.left, path, target, ans, sumPath)
            if root.right!=None:
                dfs(root.right, path, target, ans, sumPath)
            path.pop()
            return 
        
        path = []
        ans = []
        dfs(root, path, target, ans, 0)
        return ans
            