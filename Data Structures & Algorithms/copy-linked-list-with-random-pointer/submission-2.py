"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dict_copy = defaultdict(lambda: Node(0))
        dict_copy[None] = None

        curr = head
        while curr:
            
            dict_copy[curr].val = curr.val
            dict_copy[curr].next = dict_copy[curr.next]
            dict_copy[curr].random = dict_copy[curr.random]
            curr = curr.next
        
        return dict_copy[head]
