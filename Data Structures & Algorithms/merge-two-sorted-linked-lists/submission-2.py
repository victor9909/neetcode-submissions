# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        head = dummy
        while list1 and list2:
            v1 = list1.val
            v2 = list2.val
            if v1 > v2:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return head.next
