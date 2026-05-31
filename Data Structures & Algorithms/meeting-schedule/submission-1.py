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
            if i.start in hm:
                return False 
            for j in range(i.start, i.end):
                hm[j] = 1
        return True
            