# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        l, r = dummy, dummy

        for _ in range(left - 1):
            l = l.next
        
        for _ in range(right):
            r = r.next


        tmp1, tmp2 = r.next, l.next
        r.next = l.next = None
        
        prev = None
        curr = tmp2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        l.next = prev
        tmp2.next = tmp1

        return dummy.next

        
