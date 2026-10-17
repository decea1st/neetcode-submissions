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
        # tail = None, head = 2
        #  -> 2   tail = 2, head = 4   -> 2 -> 10   tail = 10
        #  -> 2 -> 10 -> 4   tail = 4, head = 6   -> 2 -> 10 -> 4 -> 8   tail = 8
        for i, node in enumerate(nodes):
            tail.next = head
            tail, head = tail.next, head.next
            tail.next = node
            tail = tail.next
        if n % 2 != 0:
            tail.next = head
            tail = tail.next
        tail.next = None
        