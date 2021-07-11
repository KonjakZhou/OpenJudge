# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans = list()
        nodeStack = []
        visitStack = []

        cur = root
        visited = False
        while cur != None :
            if  visited:
                ans.append(cur.val)
            else:
                if cur.right != None:
                    nodeStack.append(cur.right)
                    visitStack.append(False)
                
                
                nodeStack.append(cur)
                visitStack.append(True)

                if cur.left != None:
                    nodeStack.append(cur.left)
                    visitStack.append(False)
            
            if len(nodeStack)>0:
                cur = nodeStack.pop()
                visited = visitStack.pop()
            else:
                cur=None
        return ans