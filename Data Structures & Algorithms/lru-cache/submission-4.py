class Node:

    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.cache = {}

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.delete(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if self.capacity < len(self.cache):
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
        




