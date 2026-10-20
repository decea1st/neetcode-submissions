"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = head
        nodeMap = {}
        tail = Node(0)
        
        copy = tail
        while start:
            copy.next = Node(start.val)
            nodeMap[start] = copy.next
            copy, start = copy.next, start.next
        nodeMap[None] = None
        
        copy, start = tail.next, head
        while start:
            rand = nodeMap[start.random]
            copy.random = nodeMap[start.random]
            copy, start = copy.next, start.next
            
        return tail.next