# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        tail = D = ListNode()
        while head1 and head2:
            if head1.val <= head2.val:
                D.next, head1 = head1, head1.next
            else:
                D.next, head2 = head2, head2.next
            D = D.next
        D.next = head1 or head2
        return tail.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i < len(lists)-1:
                    merged.append(self.merge(lists[i], lists[i+1]))
                elif i == len(lists)-1:
                    merged.append(lists[i])
            lists = merged
        return lists[0] if lists else None
            