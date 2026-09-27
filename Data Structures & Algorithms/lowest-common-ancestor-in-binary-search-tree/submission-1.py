# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    lca = None
    def dfs(self, root, p, q):
        if root is None: 
            return
        # At each Node I can answer the question: Am I currently between my p and q (inclusive)?. If yes, set lca and return.
        # If I'm between p and q, then going in either direction means I'm splitting away from one, and will no longer be at an ancestor
        if ((root.val == p.val or root.val == q.val) or (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val)):
            Solution.lca = root
            return
        self.dfs(root.left, p, q)
        self.dfs(root.right, p, q)
        return
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        Solution.lca = None
        self.dfs(root, p, q)
        return self.lca
        