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
        # Start at head, I can copy this node. Then I can store it and mark that there's no random yet. 
        # copy : real, { 7, 4, 5}
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