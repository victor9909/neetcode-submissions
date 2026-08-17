class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = {}
        for n in nums:
            dict_nums[n] = dict_nums.get(n, 0) + 1
        
        len_arr = len(nums)
        arr = [[] for _ in range(len_arr + 1)]
        for key in dict_nums:
            arr[dict_nums[key]].append(key)
        
        res = []
        for l in arr[::-1]:
            for n in l:
                res.append(n)
                if len(res) == k:
                    return res
        