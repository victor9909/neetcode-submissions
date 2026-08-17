class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows = m
        cols = n
        directions = [(0, 1), (1, 0)]

        # Time 2^(m * n)
        # Space (m * n)
        cache = {}

        def dfs(r, c):
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            if r == rows - 1 and c == cols - 1:
                cache[(r, c)] = 1
                return cache[(r, c)]

            if r == rows or c == cols:
                return 0
            
            count = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            cache[(r, c)] = count
            return count
        
        return dfs(0, 0)