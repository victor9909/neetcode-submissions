class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[0] * n for _ in range(m)]

        def dfs(r, c):

            if r not in range(m) or c not in range(n):
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]

            if r == m - 1 and c == n - 1:
                return 1
            
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]
        
        def dp():
            prev_row = [0] * n

            for r in range(m):
                curr_row = [0] * n
                curr_row[n - 1] = 1
                for c in range(n-2, -1, -1):
                    curr_row[c] = curr_row[c + 1] + prev_row[c]
                prev_row = curr_row
            return prev_row[0]


        return dp()
