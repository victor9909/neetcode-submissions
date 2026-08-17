class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        num_ele = len(nums) // 3
        dict_nums = defaultdict(int)
        res = set()
        for n in nums:
            dict_nums[n] += 1
            if dict_nums[n] > num_ele:
                res.add(n)
        
        return list(res)