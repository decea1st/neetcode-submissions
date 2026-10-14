# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    tStr = [] # 1,2,3,n,n,4,5,n,n,n,n
    def stringBFS(self, root):
        nodeQ = deque([root])
        self.tStr.append(str(root.val) + ",")
        while nodeQ:
            valid_nodes = []
            for x in [nodeQ[0].left, nodeQ[0].right]:
                if x is None:
                    self.tStr.append("n,")
                else:
                    self.tStr.append(str(x.val) + ",")
                    valid_nodes.append(x)
            nodeQ.extend(valid_nodes)
            nodeQ.popleft()
        return "".join(self.tStr)[:-1]

    def unravelBFS(self, string):
        tree = string.split(",") # 1 2 3 n n 4 5 6 7 8 9
        n = len(tree)
        childPtr = 1
        root = TreeNode(int(tree[0]))
        nodeQ = deque([root])
        while nodeQ:
            if childPtr < n and tree[childPtr] != "n":
                left = TreeNode(int(tree[childPtr]))
                nodeQ[0].left = left
                nodeQ.append(left)
            else: left = None
            childPtr += 1
            if childPtr < n and tree[childPtr] != "n":
                right = TreeNode(int(tree[childPtr]))
                nodeQ[0].right = right
                nodeQ.append(right)
            else: right = None
            childPtr += 1
            nodeQ.popleft()
        return root

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.tStr = []
        if root is None:
            return ""
        return self.stringBFS(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        return self.unravelBFS(data)
