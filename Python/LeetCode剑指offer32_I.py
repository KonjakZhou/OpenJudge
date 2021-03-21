# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []

        queue = [root]
        ans = list()
        
        head = 0
        while head<len(queue):
            t = queue[head]
            ans.append(t.val)
            head += 1
            
            if t.left != None:
                queue.append(t.left)
            if t.right != None:
                queue.append(t.right)
        return ans 
        

