class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        times = 0
        while q and fresh:
            len_q = len(q)
            times += 1
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] in [0, 2]
                    ):
                        continue
                    
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
        return times if not fresh else -1

