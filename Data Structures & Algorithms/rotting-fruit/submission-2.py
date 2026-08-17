class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        visit = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        time = 1
        while q and fresh:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if(
                        0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1
        return time - 1 if not fresh else -1
                

