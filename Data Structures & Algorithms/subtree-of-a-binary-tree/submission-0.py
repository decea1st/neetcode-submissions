# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root):
        if root is None:
            return None
        myArray = [root.val, self.dfs(root.left), self.dfs(root.right)]
        return myArray
    def isSameTree(self, root, subRoot):
        return self.dfs(subRoot) == self.dfs(root)

    def findStartNode(self, root, subRoot):
        if root is None:
            return False
        if root.val == subRoot.val:
            res = self.isSameTree(root, subRoot)
            if res:
                return True
        leftRes = self.findStartNode(root.left, subRoot)
        rightRes = self.findStartNode(root.right, subRoot)
        if leftRes or rightRes:
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.findStartNode(root, subRoot)