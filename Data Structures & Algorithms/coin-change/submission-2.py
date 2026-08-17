class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}

        def dfs(step_amn):

            if step_amn in cache:
                return cache[step_amn]

            if step_amn == 0:
                return 0
            
            if step_amn < 0:
                return float("inf")
            
            step_res = float("inf")
            for c in coins:
                step_res_l = 1 + dfs(step_amn - c)
                step_res = min(step_res, step_res_l)
            
            cache[step_amn] = step_res

            return step_res
        
        res = dfs(amount)
        return -1 if res == float("inf") else res
        


            
        
        