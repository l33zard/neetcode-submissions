"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        hm = {}
        for i in intervals:
            for t in range(i.start, i.end):
                if t in hm:
                    return False
                hm[t] = 1
        return True