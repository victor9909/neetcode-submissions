class ListNode():

    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prev
        prev.next, nxt.prev = node, node
    
    def _delete(self):
        first = self.left.next
        nxt = first.next
        nxt.prev = self.left
        self.left.next = nxt

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k:
            return False
        self.size += 1
        node = ListNode(value)
        self._insert(node)
        return True
        
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        self._delete()
        return True

    def Front(self) -> int:
        return self.left.next.val if self.size else -1

    def Rear(self) -> int:
        return self.right.prev.val if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()