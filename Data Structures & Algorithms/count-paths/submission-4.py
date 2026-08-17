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
        
        #return dfs(0, 0)

        def dp():
            
            prev_row = [0] * cols
            prev_row[-1] = 1

            for r in range(rows):
                curr_row = [0] * cols
                curr_row[-1] = 1
                for c in range(cols - 2, -1, -1):
                    curr_row[c] = prev_row[c] + curr_row[c + 1]
                prev_row = curr_row
            return prev_row[0]
        
        return dp()

            







