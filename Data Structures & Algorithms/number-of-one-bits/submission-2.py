class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ones = 0
        for i in range(32):
            if n & 1 << i:
                ones += 1
        return ones