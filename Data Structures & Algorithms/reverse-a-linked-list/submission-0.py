# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # head = [0,1,2,3] 0 -> 1 -> 2 -> 3 -> None
        # prev = None, curr = head
        # tmp = curr.next curr.next = prev prev = curr
        # tmp = -> 1, curr.next = prev (0 -> None), prev = 0
        # tmp = -> 2, 1 -> 0 -> None, prev = 1
        # ...

        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev