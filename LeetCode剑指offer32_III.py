# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        def bfs(root):
            ans = []
            ans_tmp = []
            head = 0
            cur_depth = 0
            queue = [(root, 0)]
            
            while (head<len(queue)):
                cur_node, depth = queue[head]
                head += 1
                if cur_depth != depth:
                    ans.append(ans_tmp)
                    ans_tmp = [cur_node.val]
                    cur_depth = depth
                else:
                    ans_tmp.append(cur_node.val)
                
                if cur_node.left != None:
                    queue.append((cur_node.left, depth+1))
                if cur_node.right != None:
                    queue.append((cur_node.right, depth+1))
            ans.append(ans_tmp)
            return ans
        
        if root==None:
            return []
        ans = bfs(root)
        for i, ans_tmp in enumerate(ans):
            if i % 1 == 1:
                ans_tmp.reverse()
        return ans
    