class Node():

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # delete
            self.delete(self.cache[key])
            # insert
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.delete(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])

        while len(self.cache) > self.cap:
            lru = self.left.next
            del self.cache[lru.key]
            self.delete(lru)




        
