class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or 
                (r, c) in visit or
                grid[r][c] == 0
            ):
                return 0

            visit.add((r, c))
            res = 1
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)

            return res
        
        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))

            area = 1
            while q:
                len_q = len(q)
                for _ in range(len_q):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if(
                            row not in range(rows) or
                            col not in range(cols) or
                            grid[row][col] == 0 or
                            
                            (row, col) in visit
                        ):
                            continue
                        area += 1
                        visit.add((row, col))
                        q.append((row, col))
            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res
            
