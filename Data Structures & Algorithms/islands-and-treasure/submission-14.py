class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dist = 0
        while q:
            len_q = len(q)
            for _ in range(len_q):
                r, c = q.popleft()
                if(
                    r not in range(rows) or
                    c not in range(cols) or
                    grid[r][c] == -1 or
                    (r, c) in visit
                ):
                    continue
                
                visit.add((r, c))
                if grid[r][c] != 0:
                    grid[r][c] = dist
                
                for dr, dc in directions:
                    q.append((r + dr, c + dc))
            dist += 1
        
                