class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # ..0001 
        # ..0001
        # ..0010
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            carry = a & b
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        return a if a <= max_int else ~(a ^ mask)
