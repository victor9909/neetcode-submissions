# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse(l):
            curr = l
            prev = None

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
        
            return prev
        

        dummy = ListNode()
        dummy.next = head

        left -= 1
        l, r = dummy, dummy
        while left > 0:
            l = l.next
            left -= 1
        
        while right > 0:
            right -= 1
            r = r.next
        
        tmp_l, tmp_r = l.next, r.next
        l.next = r.next = None

        reversed_list = reverse(tmp_l)
        l.next = reversed_list
        
        while reversed_list.next:
            reversed_list = reversed_list.next
        
        reversed_list.next = tmp_r
        return dummy.next
        





