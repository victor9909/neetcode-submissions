class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnt = Counter(tasks)
        max_h = []
        for k in cnt:
            heapq.heappush(max_h, -1 * cnt[k])
        
        q = deque()
        time = 0

        while q or max_h:

            time += 1
            if not max_h:
                time = q[0][0]
            else:
                cnt = heapq.heappop(max_h) + 1
                if cnt:
                    q.append([time + n, cnt])
            if q and q[0][0] == time:
                heapq.heappush(max_h, q.popleft()[1])
        return time



