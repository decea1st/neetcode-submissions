# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # res = None
    # def traverseReverse(self, head, prev):
    #     if head is None:
    #         self.res = prev
    #         return
    #     self.traverseReverse(head.next, head)
    #     head.next = prev
    #     return

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # self.traverseReverse(head, None)
        # return self.res
        
        # Iterative
        curr, prev = head, None
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev