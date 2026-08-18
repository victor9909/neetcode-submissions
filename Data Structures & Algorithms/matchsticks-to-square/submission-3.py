class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        matchsticks.sort(reverse=True)
        target = sum(matchsticks) // 4
        if matchsticks[0] > target:
            return False
        
        bucket = [0] * 4
        
        def backtrack(idx):

            if idx == len(matchsticks):
                return True
            
            stick = matchsticks[idx]
            for i in range(4):

                if bucket[i] + stick > target:
                    continue
                
                bucket[i] += stick
                if backtrack(idx + 1):
                    return True
                
                bucket[i] -= stick
                if bucket[i] == 0:
                    break
            
            return False
        
        return backtrack(0)
                
        