class Solution:
    def reverse(self, x: int) -> int:
        
        x_rev = []
        neg = x < 0

        if neg:
            x = x * -1

        while x > 0:
            curr = x % 10
            x_rev.append(curr)
            x = x // 10
        
        def sum_num(a, b):
            carry = (a & b) << 1
            curr_s = a ^ b
            
            while carry:
                tmp = curr_s ^ carry
                carry = (curr_s & carry) << 1
                curr_s = tmp
            return curr_s
        
        idx = 0
        curr = 0
        for n in x_rev[::-1]:
            curr = sum_num(curr, n * pow(10, idx))
            idx += 1
        
        curr = -1 * curr if neg else curr
        return curr if -2**31 <= curr <= 2**31 - 1 else 0






