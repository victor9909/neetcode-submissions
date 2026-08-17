class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i, curr):
            nonlocal target

            if i == len(nums) and sum(curr) == target:
                return 1

            if i >= len(nums):
                return 0
            
            
            
            
                
            
            n_sum = 0
            curr.append(nums[i])
            n_sum += dfs(i + 1, curr)
            curr.pop()

            curr.append(-1 * nums[i])
            n_sum += dfs(i + 1, curr)
            curr.pop()

            return n_sum
        
        return dfs(0, [])