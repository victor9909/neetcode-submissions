"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # Mappo gli eventi di ingresso/uscita
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        # numero precedente di sale occupate
        # sto raccogliendo lungo l'asse x gli eventi
        prev = 0
        res = 0
        for key in sorted(mp.keys()):
            prev += mp[key]
            res = max(res, prev)
        return res
        