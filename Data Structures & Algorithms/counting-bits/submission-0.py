class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []
        for i in range(n+1):
            one = 0
            while i > 0:
                if i & 1 == 1:
                    one += 1
                i = i >> 1
            res.append(one)
        return res