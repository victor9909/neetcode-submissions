class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        while l <= r:
            cur_s = numbers[l] + numbers[r]
            if cur_s > target:
                r -= 1
            elif cur_s < target:
                l += 1
            else:
                return [l + 1, r + 1]