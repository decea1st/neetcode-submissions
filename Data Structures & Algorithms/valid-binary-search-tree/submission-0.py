# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def dfs(self, root, lowerLimit, upperLimit):
        if root is None:
            return True
        if root.val <= lowerLimit or root.val >= upperLimit:
            return False
        return self.dfs(root.left, lowerLimit, root.val) and self.dfs(root.right, root.val, upperLimit)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))