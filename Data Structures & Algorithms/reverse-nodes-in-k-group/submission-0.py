# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, k):
        p1, p2 = None, head
        for _ in range(k):
            p2.next, p1, p2 = p1, p2, p2.next
        return p1 # With 1 2 3 it returns 3

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        D = prev = ListNode()

        count, nxtSeg, counter = 1, head, head
        while nxtSeg:
            for _ in range(k-1):
                counter = counter.next
                if counter is None: break
                count += 1
            if count == k:
                firstNode = nxtSeg # Head, 1
                nxtSeg = counter = counter.next # 4
                count = 1
                prev.next = self.reverse(firstNode, k)
                prev = firstNode
            else:
                prev.next = nxtSeg
                break
        return D.next

