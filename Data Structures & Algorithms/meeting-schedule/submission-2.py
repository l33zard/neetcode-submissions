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
            for j in range(i.start, i.end):
                if j in hm:
                    return False
                hm[j] = 1
        return True
