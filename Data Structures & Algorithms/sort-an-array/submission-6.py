class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        min_a, max_a = min(nums), max(nums)

        for n in nums:
            count[n] += 1

        res = []
        for n in range(min_a, max_a + 1):
            while count[n] > 0:
                count[n] -= 1
                res.append(n)
        return res 