# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Porta right n posizioni avanti
        for _ in range(n):
            right = right.next

        # Sposta entrambi finché right arriva alla fine
        while right:
            left = left.next
            right = right.next

        # Elimina il nodo
        left.next = left.next.next

        return dummy.next