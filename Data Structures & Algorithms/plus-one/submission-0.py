class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num_str = ""
        for d in digits:
            num_str += str(d)
        
        num = int(num_str) + 1
        num_str = str(num)
        res = []
        for c in num_str:
            res.append(c)

        return res