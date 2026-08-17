# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        slow.next = prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # [0, 1, 2, 3, 4, 5, 6]
        # 0 1 2 3
        # 6 5 4
        curr = head
        while curr and prev:
            tmp1, tmp2 = curr.next, prev.next
            curr.next = prev
            prev.next = tmp1
            curr, prev = tmp1, tmp2




        
