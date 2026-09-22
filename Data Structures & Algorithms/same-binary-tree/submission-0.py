# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root is None:
            return -1
        myArray = [root.val, self.dfs(root.left), self.dfs(root.right)]
        return myArray
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        first = self.dfs(p)
        second = self.dfs(q)
        return first == second