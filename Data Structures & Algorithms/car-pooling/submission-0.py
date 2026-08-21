class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        mp = {}
        for trip in trips:
            if trip[1] in mp:
                mp[trip[1]] += trip[0]
            else:
                mp[trip[1]] = trip[0]

            if trip[2] in mp:
                mp[trip[2]] += -1 * trip[0]
            else:
                mp[trip[2]] = -1 * trip[0]
            
        keys = sorted(mp.keys())
        cnt = 0
        for k in keys:
            cnt += mp[k]
            if cnt > capacity:
                return False
        return True