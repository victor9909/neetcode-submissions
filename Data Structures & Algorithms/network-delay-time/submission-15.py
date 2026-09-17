class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        min_h = []
        heapq.heappush(min_h, (0, k))
        visit = set()

        adj_list = {i:[] for i in range(1, n + 1)}
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        time = 0
        while min_h:            
            w, u = heapq.heappop(min_h)
            
            if u in visit:
                continue
            
            visit.add(u)
            time = w
            for v, z in adj_list[u]:    
                heapq.heappush(min_h, (z + w, v))
        
        return time if len(visit) == n else -1
