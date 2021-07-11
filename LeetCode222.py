# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.height = 0
        self.nodes = list()
        self.flag = 0

    def countNodes(self, root: TreeNode) -> int:
        node = root
        if node is None:
            return 0
        while node.left is not None:
            self.height += 1
            node = node.left

        self.nodes = [0 for _ in range(self.height+1)]
        self.dfs(root, 0)

        ans = pow(2, self.height) -1 + self.nodes[self.height]
        return ans

    def dfs(self, node: TreeNode, height: int):
        if self.flag == 1:
            return

        self.nodes[height] += 1

        if node.left is not None:
            self.dfs(node.left, height + 1)
            if node.right is not None:
                self.dfs(node.right, height + 1)
            else:
                self.flag = 1
                return
        else:
            if height == self.height - 1:
                self.flag = 1
                return
        return


if __name__ == '__main__':
    total = 7
    treeArray = [TreeNode(i) for i in range(total)]

    for i in range(total):
        try:
            treeArray[i].left = treeArray[i * 2 + 1]
            treeArray[i].right = treeArray[i * 2 + 2]
        except IndexError:
            pass
    solution = Solution()
    root = treeArray[0]
    solution.countNodes(root)
