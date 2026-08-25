class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        max_h = []
        for c, cnt in [('a', a), ('b', b), ('c', c)]:
            if cnt != 0:
                heapq.heappush(max_h, (-cnt, c))
        
        res = []
        while max_h:
            cnt, c = heapq.heappop(max_h)
            if len(res) >= 2 and res[-1] == c and res[-2] == c:
                if not max_h:
                    break
                cnt2, c2 = heapq.heappop(max_h)
                res.append(c2)
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(max_h, (cnt2, c2))
                heapq.heappush(max_h, (cnt, c))
            else:
                res.append(c)
                cnt += 1
                if cnt != 0:
                    heapq.heappush(max_h, (cnt, c))
        return "".join(res)
