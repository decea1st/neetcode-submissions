# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    res = None
    def dfs(self, root, k):
        if root is None:
            return 0
        if self.res is not None:
            return
        self.dfs(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
        self.dfs(root.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None
        self.dfs(root, k)
        return self.res