# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()

        carry = 0
        s1, s2, s3 = l1, l2, tail
        while s1 or s2 or carry:
            if s1:
                n1 = s1.val
                s1 = s1.next
            else: n1 = 0

            if s2:
                n2 = s2.val
                s2 = s2.next
            else: n2 = 0

            n3 = n1 + n2 + carry
            s3.next = ListNode(n3 % 10)
            s3 = s3.next
            carry = n3 // 10
        return tail.next