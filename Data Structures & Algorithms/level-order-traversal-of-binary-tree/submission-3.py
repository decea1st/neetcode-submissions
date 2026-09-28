# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    res = [] # [[1],]
    def bfs(self, root):
        nodeQ = deque([root]) # [root]
        while nodeQ: # [root]
            level = list(nodeQ)
            subArr = []
            for node in level:
                subArr.append(node.val)
                valid_nodes = [nodes for nodes in [node.left, node.right] if nodes is not None]
                nodeQ.extend(valid_nodes)
                nodeQ.popleft()
            self.res.append(subArr)
        return self.res
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        if root is None:
            return []
        return self.bfs(root)