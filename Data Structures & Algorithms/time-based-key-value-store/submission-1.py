class TimeMap:

    def __init__(self):
        
        self.key = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.key:
            return res
        
        values = self.key[key]
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1

        return res 

