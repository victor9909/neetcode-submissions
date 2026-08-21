"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] += -1
        
        res = 0
        cnt = 0
        i, j = 0, 0
        sorted_k = sorted(mp.keys())
        for k in sorted_k:
            cnt += mp[k]
            res = max(res, cnt)

        return res