# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        while list1 and list2:

            v1 = list1.val
            v2 = list2.val
            if v1 > v2:
                curr.next = ListNode(v2)
                list2 = list2.next
            else:
                curr.next = ListNode(v1)
                list1 = list1.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next
            
