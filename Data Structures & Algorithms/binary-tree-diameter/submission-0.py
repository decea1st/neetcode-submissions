# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def fuckyou(self, root):
        if root is None:
            return 0
        leftArm = self.fuckyou(root.left)
        rightArm = self.fuckyou(root.right)
        diameter = leftArm + rightArm
        self.maxDiameter = max(self.maxDiameter, diameter)
        return 1 + max(leftArm, rightArm)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.fuckyou(root)
        return self.maxDiameter