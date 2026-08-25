class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnt = Counter(tasks)
        max_h = []
        for k, v in cnt.items():
            heapq.heappush(max_h, -v)
        
        q = deque()
        time = 0

        while max_h or q:
            time += 1

            if not max_h:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_h)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_h, q.popleft()[0])
        return time


