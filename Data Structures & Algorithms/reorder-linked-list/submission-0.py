# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # head = [2,4,6,8,10]
        # first = [2, 4] second = [6,8,10]
        # first = [2, 4] second = [10, 8, 6]
        # first = [2, 4, 6] second = [10, 8]
        # final = [2, 10, 4, 8, 6]

        # divide the list
        slow = head
        fast = head
        # head = [2,4,6,8,10]
        #.            s
        #.                 f

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # revert second
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        




