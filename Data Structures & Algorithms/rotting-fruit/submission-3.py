class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visit = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        fresh = 0

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while q and fresh:
            len_q = len(q)
            for _ in range(len_q):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if(
                        nr not in range(rows) or
                        nc not in range(cols) or
                        grid[nr][nc] == 0 or
                        (nr, nc) in visit
                    ):
                        continue
                    
                    fresh -= 1
                    q.append((nr, nc))
                    visit.add((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1