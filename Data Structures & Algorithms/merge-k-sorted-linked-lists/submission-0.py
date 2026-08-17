# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_list(l1, l2):
            
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                
                if l1.val > l2.val:
                    curr.next = l2
                    l2 = l2.next
                else:
                    curr.next = l1
                    l1 = l1.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            
            return dummy.next

        while len(lists) > 1:
            l1, l2 = lists.pop(), lists.pop()
            l3 = merge_list(l1, l2)
            print(l3)
            lists.append(l3)
        
        return lists[-1] if lists else None


        
        