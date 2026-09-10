class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr = 0
        dict_pre = defaultdict(int)
        dict_pre[0] = 1
        res = 0
        for n in nums:
            curr += n
            res += dict_pre[curr - k]
            dict_pre[curr] += 1

        return res