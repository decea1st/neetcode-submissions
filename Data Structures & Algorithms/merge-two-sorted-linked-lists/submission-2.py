# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSort(self, list1, list2):
        match (list1, list2):
            case (None, None): return None
            case (None, _): return list2
            case (_, None): return list1

        if list1.val <= list2.val: res, curr, anchor = list1, list1, list2
        else: res, curr, anchor = list2, list2, list1
        while list1 is not None or list2 is not None:
            while curr.val <= anchor.val:
                prev = curr
                curr = curr.next
                if curr is None:
                    prev.next = anchor
                    return res
            prev.next = anchor
            anchor, curr = curr, anchor
        return self.res

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(list1, list2)