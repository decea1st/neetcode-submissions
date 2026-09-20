# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countDepth(self, root):
        if root is None: return 0

        left = self.countDepth(root.left)
        right = self.countDepth(root.right)
        difference = abs(left - right)

        if left < 0 or right < 0:
            return -1
        if difference < 2:
            return 1 + max(left, right)
        else:
            return -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        res = self.countDepth(root)
        if res < 0:
            return False
        else:
            return True