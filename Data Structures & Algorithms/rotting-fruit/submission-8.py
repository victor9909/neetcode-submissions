class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
        
        time = 0
        while q and fresh:
            len_q = len(q)
            time += 1
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
                    
                    fresh -= 1
                    visit.add((row, col))
                    q.append((row, col))
        
        return time if fresh == 0 else -1

