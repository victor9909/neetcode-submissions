class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        min_v, max_v = min(nums), max(nums)
        for val in nums:
            count[val] += 1
        
        idx = 0
        for val in range(min_v, max_v + 1):
            while count[val] > 0:
                nums[idx] = val
                idx += 1
                count[val] -= 1
        return nums