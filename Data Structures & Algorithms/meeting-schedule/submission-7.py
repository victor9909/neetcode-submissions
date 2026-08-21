"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x: x.start)
        cnt = 0
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        i, j = 0, 0
        while i < len(intervals) and j < len(intervals):
            if starts[i] < ends[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            if cnt > 1:
                return False
        return True

