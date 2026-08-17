class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        len_n = len(nums)
        res = []
        for i in range(2 * len_n):
            res.append(nums[i%len_n])
        return res