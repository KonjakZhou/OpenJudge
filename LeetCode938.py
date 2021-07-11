# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int):
        def preOrder(root, ans):
            if root==None:
                return
            if root!=None:
                if low<=root.val<=high:
                    ans[0] += root.val
                    preOrder(root.left, ans)
                    preOrder(root.right, ans)
                    return
                if root.val<low:
                    preOrder(root.right, ans)
                    return
                if root.val>high:
                    preOrder(root.left, ans)
                    return

        ans = [0]
        preOrder(root, ans)
        return ans[0]

        