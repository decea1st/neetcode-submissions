# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while head is not None:
            for _ in range(2):
                fast = fast.next
                if fast is None: return False
            slow = slow.next
            if fast is slow: return True
        return False