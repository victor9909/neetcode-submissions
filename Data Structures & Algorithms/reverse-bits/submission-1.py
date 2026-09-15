class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = ""
        mask = 1
        for i in range(32):
            if n & mask << i:
                binary += "1"
            else:
                binary += "0"
        
        return int(binary,2)