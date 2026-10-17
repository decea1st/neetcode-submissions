# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        visited = set([head])
        head = head.next

        while head is not None and head.next is not None:
            if head in visited: return True
            visited.add(head)
            head = head.next

        return False