class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visit = set()
        dp = {}  

        def dfs(i, j, prev):
            
            if(
                i not in range(rows) or
                j not in range(cols) or
                (i, j) in visit or
                prev >= matrix[i][j]
            ):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]

            res = 0
            visit.add((i, j))
            for dr, dc in directions:
                res = max(res, dfs(i + dr, j + dc, matrix[i][j]))
            visit.remove((i, j))
            dp[(i, j)] = res + 1

            return dp[(i, j)]

        
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, float("-inf")))
        return res


