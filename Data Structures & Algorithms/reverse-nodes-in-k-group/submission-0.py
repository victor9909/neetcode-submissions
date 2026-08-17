# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(curr):

            prev = None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
    
        
        lists = []
        l = head
        curr = head
        cnt = k
        last = None
        while curr:
            tmp = curr.next
            cnt -= 1
            if cnt == 0:
                cnt = k
                lists.append(l)
                l = curr.next
                curr.next = None
            if tmp == None:
                last = l
            curr = tmp 
        
        reversed_l = []
        for l in lists:
            curr = reverse(l)
            reversed_l.append(curr)

        if last:
            reversed_l.append(last)

        dummy = ListNode()
        curr = dummy
        for r in reversed_l:
            curr.next = r
            while curr and curr.next:
                curr = curr.next
        
        return dummy.next
            

