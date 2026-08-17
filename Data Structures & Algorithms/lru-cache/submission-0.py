class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}

        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            self.remove(self.lru_cache[key])
            self.insert(self.lru_cache[key])
            return self.lru_cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            self.remove(self.lru_cache[key])
        
        self.lru_cache[key] = Node(key, value)
        self.insert(self.lru_cache[key])

        if len(self.lru_cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.lru_cache[lru.key]
            





        
