class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        mask = 1
        for n in range(n + 1):
            one = 0
            for i in range(32):
                if n & (mask << i):
                    one += 1
            res.append(one)
        return res