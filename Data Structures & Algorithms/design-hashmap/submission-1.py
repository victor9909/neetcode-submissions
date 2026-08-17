class MyHashMap:

    def __init__(self):
        self.keys_list = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        print(key)
        self.keys_list[key] = value

    def get(self, key: int) -> int:
        if self.keys_list[key] != None:
            return self.keys_list[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.keys_list[key] != None:
            self.keys_list[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)