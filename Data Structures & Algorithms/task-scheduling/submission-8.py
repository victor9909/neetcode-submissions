class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnt = Counter(tasks)
        max_h = []
        for t, v in cnt.items():
            heapq.heappush(max_h, -1* v)
        
        q = deque()
        time = 0

        while max_h or q:

            time += 1
            if q and q[0][0] == time:
                heapq.heappush(max_h, q.popleft()[1])
            
            if max_h:
                cnt = heapq.heappop(max_h)
                if cnt + 1 != 0:
                    q.append((time + 1 + n, cnt + 1))                
            
        return time
