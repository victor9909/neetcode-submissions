class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = ""
        for i in range(32):
            bit = n & 1 << i
            if bit:
                binary += "1"
            else:
                binary += "0"

        n = 0
        for i, b in enumerate(binary[::-1]):
            n += pow(2, i) * int(b)
        return n