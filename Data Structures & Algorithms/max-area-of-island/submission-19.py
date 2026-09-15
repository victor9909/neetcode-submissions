class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(r, c):

            if(
                r not in range(rows) or
                c not in range(cols) or
                grid[r][c] == 0
            ):
                return 0
            
            grid[r][c] = 0
            cnt = 0
            for dr, dc in directions:
                cnt += dfs(r + dr, c + dc)
            return cnt + 1
        
        def bfs(r, c):

            q = deque([(r, c)])
            area = 1
            grid[r][c] = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(
                        row not in range(rows) or
                        col not in range(cols) or
                        grid[row][col] == 0 
                    ):
                        continue
                    
                    area += 1
                    q.append((row, col))
                    grid[row][col] = 0

            return area

        rank = [1 for _ in range((cols * rows) + 1)]
        par = [i for i in range((cols * rows) + 1)]

        def find(u):
            p = par[u]
            while p != par[p]:
                p = par[p]
            return p
        
        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True

        def get_size(node):
            node = par[node]
            return rank[node]

        """
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    res = max(res, area)
        
        """
        def index(r, c):
            return r * cols + c

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = 1
                    atleast = True
                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if(
                            row not in range(rows) or
                            col not in range(cols) or
                            grid[row][col] == 0
                        ):
                            continue
                        
                        union(index(row, col), index(r, c))
                
                    res = max(res, get_size(index(r, c)))
        
        return res
