class ListNode():

    def __init__(self, val):
        self.val = val
        self.key = None
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left, self.right = ListNode(0), ListNode(0)
        self.left.next, self.right.prev = self.right, self.left
        self.capacity = capacity
        self.size = 0

    def _insert(self, node):
        tmp = self.left.next
        node.prev, self.left.next = self.left, node
        node.next, tmp.prev = tmp, node

    def _delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next, node.prev = None, None

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self._delete(node)
            self.size -= 1

        self.size += 1

        node = ListNode(value)
        node.key = key
        self.cache[key] = node
        self._insert(node)

        if self.size > self.capacity:
            node = self.right.prev
            del self.cache[node.key]
            self._delete(node)
            self.size -= 1

        









        
