class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or 
                        (row, col) in visit or
                        grid[row][col] == 0 
                    ):
                        continue
                    
                    visit.add((row, col))
                    fresh -= 1
                    q.append((row, col))

            time += 1
        
        return time if fresh == 0 else -1

