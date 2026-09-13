class Node():

    def __init__(self, val=None, key=None):
        self.val, self.key = val, key
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def insert(self, node):
        prev, nxt = self.left, self.left.next
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.next, node.prev = None, None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            self.size -= 1
            del self.cache[key]

        self.cache[key] = Node(value, key)
        self.insert(self.cache[key])
        self.size += 1
        while self.size > self.cap:
            lru = self.right.prev
            del self.cache[lru.key]
            self.remove(lru)
            self.size -= 1














        
