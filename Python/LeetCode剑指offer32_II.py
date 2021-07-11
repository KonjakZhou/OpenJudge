# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        def bfs(root):
            ans = []
            cur_level = 0
            queue = [(root, 0)]
            head = 0

            ans_tmp = []
            while head < len(queue):
                cur_node, depth = queue[head]
                if depth!=cur_level:
                    ans.append(ans_tmp)
                    ans_tmp = [cur_node.val]
                    cur_level+=1
                else:
                    ans_tmp.append(cur_node.val)

                head += 1
                if cur_node.left!=None:
                    queue.append((cur_node.left, depth+1))
                if cur_node.right!=None:
                    queue.append((cur_node.right, depth+1))
            ans.append(ans_tmp)
            return ans
        
        if root==None:
            return []
        return bfs(root)
                