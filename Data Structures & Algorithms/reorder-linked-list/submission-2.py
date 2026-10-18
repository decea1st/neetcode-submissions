# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        second, slow.next = prev, None
        while head is not None and second is not None:
            nxtOne, nxtTwo = head.next, second.next
            head.next = second
            head = nxtOne
            second.next = head
            second = nxtTwo
        