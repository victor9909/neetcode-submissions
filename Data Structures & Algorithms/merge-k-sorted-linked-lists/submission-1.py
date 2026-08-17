# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):

            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                v1 = l1.val
                v2 = l2.val

                node = ListNode(val=v2) if v1 > v2 else ListNode(val=v1)
                curr.next = node
                curr = curr.next
                
                if v1 > v2:
                    l2 = l2.next
                else:
                    l1 = l1.next
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            return dummy.next


        while len(lists) > 1:
            l1, l2 = lists.pop(), lists.pop()
            merged = merge(l1, l2)
            lists.append(merged)
        
        return lists[0] if lists else None

        