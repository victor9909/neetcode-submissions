class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        # [[1,4],[3,3],[2,1]]
        # (1, 4, 0)(2, 1, 2)(3, 3, 1) -> (0, 1, 2)

        # [[5,2],[4,4],[4,1],[2,1],[3,3]]
        # (5, 2, 0)(4, 4, 1)(4,1,2)(2,1,3)(3,3,4)
        
        # (2,1,3)(3,3,4)(4,1,2)(4, 4, 1)(5, 2, 0)
        pending = []
        for idx, (enq, pro) in enumerate(tasks):
            heapq.heappush(pending, (enq, pro, idx))
        
        available = []
        time = 0
        res = []
        while pending or available:
            while pending and pending[0][0] <= time:
                enq, pro, idx = heapq.heappop(pending)
                heapq.heappush(available, (pro, idx))
            
            if not available:
                time = pending[0][0]
                continue
            
            processTime, i = heapq.heappop(available)
            time += processTime
            res.append(i)
        return res
            

