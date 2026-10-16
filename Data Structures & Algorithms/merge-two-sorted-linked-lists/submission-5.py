# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeSort(self, list1, list2):
        root = res = ListNode()
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                root.next, list1 = list1, list1.next
            else:
                root.next, list2 = list2, list2.next
            root = root.next
        root.next = list1 or list2
        return res.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(list1, list2)
