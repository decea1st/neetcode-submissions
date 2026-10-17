# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes, start = [], head
        while start is not None:
            nodes.append(start)
            start = start.next
    
        nodes.reverse()
        n = len(nodes)
        nodes = nodes[:n // 2]
        tail = ListNode()
        for i, node in enumerate(nodes):
            tail.next = head
            tail, head = tail.next, head.next
            tail.next = node
            tail = tail.next
            
        if n % 2 != 0:
            tail.next = head
            tail = tail.next
        tail.next = None
        