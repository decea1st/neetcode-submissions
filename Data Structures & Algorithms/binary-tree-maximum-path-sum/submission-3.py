# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = float('-inf')
    def randomName(self, root):
        if root is None:
            return 0
        leftChain = self.randomName(root.left)
        rightChain = self.randomName(root.right)

        bestConjoined = root.val + leftChain + rightChain
        self.res = max(self.res, bestConjoined)

        bestChain = max(leftChain+root.val, rightChain+root.val)
        return bestChain if bestChain >= 0 else 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.randomName(root)
        return self.res