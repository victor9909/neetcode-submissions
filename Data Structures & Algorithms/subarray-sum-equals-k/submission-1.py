class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict_prefix = defaultdict(int)
        dict_prefix[0] = 1

        curr = 0
        res = 0

        for n in nums:

            curr += n
            diff = curr - k
            res += dict_prefix[diff]
            dict_prefix[curr] += 1
        return res
