# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def dfs(self, root):
        if root is None:
            return 0
        leftArm = self.dfs(root.left)
        rightArm = self.dfs(root.right)
        self.res = max(leftArm + rightArm, self.res)
        return max(leftArm, rightArm) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res