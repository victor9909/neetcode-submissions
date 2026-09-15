class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            len_q = len(q)
            dist += 1
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] != 2**31 - 1
                    ):
                        continue

                    grid[row][col] = dist
                    q.append((row, col))
                    