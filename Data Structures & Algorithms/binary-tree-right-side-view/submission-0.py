# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    res = []
    def bfs(self, root):
        if root is None:
            return []
        nodeQ = deque([root])
        while nodeQ:
            level = list(nodeQ)
            rightEdge = len(level)-1
            for i, node in enumerate(level):
                valid_nodes = [child for child in [node.left, node.right] if child is not None]
                nodeQ.extend(valid_nodes)
                if i == rightEdge:
                    self.res.append(node.val)
                nodeQ.popleft()
        return self.res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        return self.bfs(root)