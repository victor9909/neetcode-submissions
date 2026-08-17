class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        count_dict = defaultdict(int)
        min_val, max_val = min(nums), max(nums)
        for n in nums:
            count_dict[n] += 1
        
        res = []
        for val in range(min_val, max_val + 1):
            while count_dict[val] > 0:
                count_dict[val] -= 1
                res.append(val)
        return res

