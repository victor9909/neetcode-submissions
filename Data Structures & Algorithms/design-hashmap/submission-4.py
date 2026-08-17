class MyHashMap:

    def __init__(self):
        self.nums = [(False, False)] * 1000001

    def put(self, key: int, value: int) -> None:
        self.nums[key] = (True, value)

    def get(self, key: int) -> int:
        return self.nums[key][1] if self.nums[key][0] else -1

    def remove(self, key: int) -> None:
        self.nums[key] = (False, False)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)