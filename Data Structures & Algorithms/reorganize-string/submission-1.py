class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = Counter(s)
        max_heap = []
        for k in count:
            heapq.heappush(max_heap, [-count[k], k])
        
        res = ""
        prev = None
        while max_heap or prev:
            
            if prev and not max_heap:
                return ""

            cnt, char = heapq.heappop(max_heap)
            if res and res[-1] == char:
                return ""

            res += char
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        
        return res