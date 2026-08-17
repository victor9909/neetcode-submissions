class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
         
        rows, cols = len(grid), len(grid[0])
        visit = set()

        if grid[0][0] or grid[rows - 1][cols - 1]:
            return -1
           

        q = deque()
        q.append((0, 0))
        lenght = 1
        directions = [(-1,0),(1,0),(0,-1),(0,1),
        (-1,-1),(-1,1),(1,-1),(1,1)]

        while q:
            len_q = len(q)
            for _ in range(len_q):
                i, j = q.popleft()
                print(i, j)
                if i == rows - 1 and j == cols - 1:
                    return lenght
                if(
                    i not in range(rows) or
                    j not in range(cols) or
                    (i, j) in visit or
                    grid[i][j] == 1
                ):
                    continue
                
                visit.add((i, j))
                for dr, dc in directions:
                    q.append((i + dr, j + dc))
            lenght += 1

        return -1