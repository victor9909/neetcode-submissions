class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        pivot = math.ceil(len(nums) / 2)

        dict_n = defaultdict(int)
        for n in nums:
            dict_n[n] += 1
            if dict_n[n] >= pivot:
                return n
                