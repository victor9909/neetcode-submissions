class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visit = set()

        def dfs(r, c):
            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == "0" or
                (r, c) in visit
            ):
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)

            return
        
        def bfs(r, c):

            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                len_q = len(q)
                for _ in range(len_q):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if(
                            nr not in range(rows) or
                            nc not in range(cols) or
                            grid[nr][nc] == "0" or
                            (nr, nc) in visit
                        ):
                            continue
                        visit.add((nr, nc))
                        q.append((nr, nc))

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    #dfs(r, c)
                    bfs(r, c)
                    count += 1
        
        return count


