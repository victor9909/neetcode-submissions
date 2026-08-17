class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        dict_nums = Counter(nums)
        target = len(nums) // 3
        res = []
        for k in dict_nums:
            if dict_nums[k] > target:
                res.append(k)
        return res