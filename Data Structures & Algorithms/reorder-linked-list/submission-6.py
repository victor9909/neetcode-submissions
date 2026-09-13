# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        s, f = head, head
        while f and f.next:
            s, f = s.next, f.next.next
        
        l2 = s.next
        s.next = prev = None

        while l2:
            tmp = l2.next
            l2.next = prev
            prev = l2
            l2 = tmp
        
        curr = head
        while curr and prev:
            tmp1, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp1
            curr, prev = tmp1, tmp2





