# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        

        dummy = ListNode()
        new_l = dummy
        curr = head
        while prev and curr:
            tmp1, tmp2 = prev.next, curr.next
            new_l.next = curr
            new_l = new_l.next
            new_l.next = prev
            new_l = new_l.next
            prev, curr = tmp1, tmp2
        
        if prev:
            new_l.next = prev
        if curr:
            new_l.next = curr

        head = dummy.next
