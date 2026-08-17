class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt_nums = Counter(nums)
        max_l = max(cnt_nums.values())
        freq = [[] for _ in range(max_l + 1)]

        for key in cnt_nums:
            freq[cnt_nums[key]].append(key)
        
        res = []
        for f in freq[::-1]:
            for e in f:
                res.append(e)
                if len(res) == k:
                    return res
