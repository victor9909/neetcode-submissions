class ListNode():

    def __init__(self, val):
        self.val = val
        self.next, self.prev = None, None

class MyCircularQueue:

    def __init__(self, k: int):
        self.max_cap = k
        self.curr_len = 0
        self.l, self.r = ListNode(-1), ListNode(-1)
        self.l.next, self.r.prev = self.r, self.l

    def _insert(self, value):
        node = ListNode(value)
        prev, next = self.r.prev, self.r
        prev.next, node.next = node, self.r
        node.prev, self.r.prev = prev, node
    
    def _delete(self):
        node = self.l.next
        nxt = node.next
        node.next, node.prev = None, None
        self.l.next, nxt.prev = nxt, self.l

    def enQueue(self, value: int) -> bool:
        if self.max_cap == self.curr_len:
            return False
        self._insert(value)
        self.curr_len += 1

        return True

    def deQueue(self) -> bool:
        if self.curr_len == 0:
            return False
        self._delete()
        self.curr_len -= 1
        return True

    def Front(self) -> int:
        return self.l.next.val

    def Rear(self) -> int:
        return self.r.prev.val

    def isEmpty(self) -> bool:
        return self.curr_len == 0

    def isFull(self) -> bool:
        return self.curr_len == self.max_cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()