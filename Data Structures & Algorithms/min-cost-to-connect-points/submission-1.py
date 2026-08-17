class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        min_heap = [[0, 0]]
        heapq.heapify(min_heap)
        visit = set()

        while min_heap:
            len_min_heap = len(min_heap)
            for _ in range(len_min_heap):
                w1, n = heapq.heappop(min_heap)
                if n in visit:
                    continue
                
                visit.add(n)
                res += w1

                for w, dst in adj[n]:
                    if dst not in visit:
                        heapq.heappush(min_heap, (w, dst))
        
        return res

