# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root, k):
        flag = [False]
        def getNodeNum(root, k):
            if root is None:
                return 0
            left = root.left
            right = root.right

            rightNum = getNodeNum(right, k)
            if flag[0]:
                return rightNum
            if rightNum == k-1:
                flag[0] = True
                return root.val
            
            leftNum = getNodeNum(left, k-rightNum-1)
            if flag[0]:
                return leftNum

            return leftNum + rightNum + 1

        return getNodeNum(root, k)

def build(root, x):
    if root.val<=x:    
        if root.right is None:
            root.right = TreeNode(x)
        else:
            build(root.right, x)
    else:
        if root.left is None:
            root.left = TreeNode(x)
        else:
            build(root.left, x)
    return 
     
if __name__ == "__main__":
    numbers = [5,3,6,2,4,1]
    k = 3
    root = TreeNode(5)
    for i in range(1, len(numbers)):
        build(root, numbers[i])
    
    solution = Solution()
    print(solution.kthLargest(root, k))
