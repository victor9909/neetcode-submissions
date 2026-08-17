class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visit = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 1
        while q:
            len_q = len(q)
            for _ in range(len_q):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if(
                        nr not in range(rows) or
                        nc not in range(cols) or
                        grid[nr][nc] == -1 or
                        (nr, nc) in visit
                    ):
                        continue
                    grid[nr][nc] = dist
                    visit.add((nr, nc))
                    q.append((nr, nc))
            dist += 1
        