# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # [0, 1, 2, 3, 4, 5, 6]
        # 0 -> [0, 1, 2, 3, 4, 5, 6]
        # 0 -> [0, 1, 2, 3, 4, 5]

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
        
        curr = head
        while curr and prev:
           tmp1, tmp2 = curr.next, prev.next
           curr.next = prev
           prev.next = tmp1
           curr, prev = tmp1, tmp2
        


