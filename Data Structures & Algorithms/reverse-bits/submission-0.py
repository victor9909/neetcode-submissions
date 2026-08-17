class Solution:
    def reverseBits(self, n: int) -> int:
        
        tmp = []
        while n > 0:
            tmp.append(n & 1)
            n = n >> 1
        
        start_idx = 31
        res = 0
        for n in tmp:
            res += pow(2, start_idx) * n
            start_idx -= 1
        return res
