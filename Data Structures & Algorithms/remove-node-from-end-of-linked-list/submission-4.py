# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = ListNode(0, head)

        target, locator = head, head
        for _ in range(n): locator = locator.next
        
        prev = tail
        while locator:
            prev = target
            target, locator = target.next, locator.next
        
        prev.next, target.next = target.next, None
        return tail.next