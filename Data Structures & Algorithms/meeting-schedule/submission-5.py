"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:


        res = 1
        events = defaultdict(int)
        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1
        
        cnt = 0
        for time in sorted(events):
            cnt += events[time]
            res = max(cnt, res)
        
        return res == 1

