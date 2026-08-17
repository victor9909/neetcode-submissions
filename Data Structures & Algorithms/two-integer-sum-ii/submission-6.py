class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l, r = 0, len(numbers) - 1
        while l <= r:
            curr_s = numbers[l] + numbers[r]
            if curr_s == target:
                return [l + 1, r + 1]
            elif curr_s > target:
                r -= 1
            else:
                l += 1
        