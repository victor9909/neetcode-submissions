class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            visit.add((r, c))
            count = 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            
            return count
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r,c))

            area = 1
            while q:
                len_q = len(q)
                for _ in range(len_q):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = dr + row, dc + col
                        if(
                            nr not in range(rows) or
                            nc not in range(cols) or
                            grid[nr][nc] == 0 or
                            (nr, nc) in visit
                        ):
                            continue
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1
            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    #area = dfs(r, c)
                    area = bfs(r, c)
                    res = max(area, res)
        
        return res


