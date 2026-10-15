# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    res = None
    def mergeSort(self, list1, list2):
        match (list1, list2):
            case (None, None): return None
            case (None, _): return list2
            case (_, None): return list1

        if list1.val <= list2.val:
            root = ListNode(list1.val)
            list1 = list1.next
        else:
            root = ListNode(list2.val)
            list2 = list2.next
        self.res = root

        while list1 is not None or list2 is not None:
            if (list1 is not None and list2 is None) or (list1 is not None and list1.val <= list2.val):
                root.next = ListNode(list1.val)
                root = root.next
                list1 = list1.next
            else:
                root.next = ListNode(list2.val)
                root = root.next
                list2 = list2.next
        return self.res

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(list1, list2)