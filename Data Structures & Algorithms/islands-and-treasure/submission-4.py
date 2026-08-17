class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c))
        
        dist = 0
        def addRoom(r, c):
            if(
                r < 0 or c < 0 or r == rows or c == cols or
                grid[r][c] == -1 or (r, c) in visit
            ):
                return
            
            q.append((r, c))
            visit.add((r, c))

        directions = [[0, 1], [0, -1], [1, 0],[-1, 0]]
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dr, dc in directions:
                    addRoom(row + dr, col + dc)
            dist += 1
    

                
                    
