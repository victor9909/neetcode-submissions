class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        nums_set = Counter(nums)
        min_n = min(nums)
        max_n = max(nums)
        res = []
        for i in range(min_n, max_n + 1):
            while i in nums_set and nums_set[i] > 0:
                res.append(i)
                nums_set[i] -= 1
        return res