class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        dist = 1
        while q:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] == -1 or
                        (row, col) in visit
                    ):
                        continue
                    q.append((row, col))
                    grid[row][col] = dist
                    visit.add((row, col))
            dist += 1
        