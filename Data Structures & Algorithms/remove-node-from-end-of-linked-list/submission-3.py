# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        newHead = prev
        curr, prev = prev, None
        for _ in range(n-1):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        else:
            newHead = newHead.next
        curr.next = None

        curr, prev = newHead, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev