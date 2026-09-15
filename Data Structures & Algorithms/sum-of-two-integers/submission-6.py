class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        carry = (a & b) << 1
        curr_s = a ^ b
        while carry:
            tmp = (curr_s ^ carry) & mask
            carry = ((curr_s & carry) << 1) & mask
            curr_s = tmp
        return curr_s if curr_s <= max_int else ~(curr_s ^ mask)