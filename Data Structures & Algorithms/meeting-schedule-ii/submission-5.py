"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        l, r = 0, 0
        res = 0
        cnt = 0
        while l < len(intervals):
            if start[l] < end[r]:
                cnt += 1
                l += 1
            else:
                cnt -= 1
                r += 1
            res = max(res, cnt)
        return res
        