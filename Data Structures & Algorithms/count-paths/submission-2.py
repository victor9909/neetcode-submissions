class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n
        directions = [(0, 1), (1, 0)]

        def dfs(r, c):
            
            if r == rows - 1 and c == cols - 1:
                return 1

            if r == rows or c == cols:
                return 0
            
            count = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            return count
        
        return dfs(0, 0)