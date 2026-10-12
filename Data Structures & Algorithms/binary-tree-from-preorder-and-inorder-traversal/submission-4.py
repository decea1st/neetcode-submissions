# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    inorderMap = {}
    preorder = inorder = []
    def buildFullTree(self, preStart, preEnd, inStart, inEnd):
        if preStart > preEnd:
            return None

        root = TreeNode(self.preorder[preStart])
        mid = self.inorderMap[self.preorder[preStart]] - inStart

        root.left = self.buildFullTree(preStart+1, preStart+mid, inStart, mid-1-inStart)
        root.right = self.buildFullTree(preStart+mid+1, preEnd, mid+1+inStart, inEnd)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i, x in enumerate(inorder): self.inorderMap[x] = i
        self.preorder, self.inorder = preorder, inorder
        return self.buildFullTree(0, len(preorder)-1, 0, len(inorder)-1)