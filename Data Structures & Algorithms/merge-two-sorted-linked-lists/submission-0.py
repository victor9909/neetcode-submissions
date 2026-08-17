# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # list1 = [1,2,4], list2 = [1,3,5]
        # dummy = [] [1]
        # dummy = [] [1, 1]
        # dummy = [] [1, 1, 2]
        # dummy = [] [1, 1, 2, 3]
        # dummy = [] [1, 1, 2, 3, 4]
        # dummy = [] [1, 1, 2, 3, 4, 5]

        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val
            if val1 > val2:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next





