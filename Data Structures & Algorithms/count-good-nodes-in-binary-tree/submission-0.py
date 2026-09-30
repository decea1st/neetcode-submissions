# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    def dfs(self, root, highest):
        if root is None:
            return
        if root.val >= highest:
            self.count += 1
        currHighest = max(highest, root.val)
        self.dfs(root.left, currHighest)
        self.dfs(root.right, currHighest)
        return

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.count