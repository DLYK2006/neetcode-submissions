"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i=1
        if intervals:
            end=intervals[0].end
        while i<len(intervals):
            if end>intervals[i].start:
                return False
            end=intervals[i].end
            i+=1
        return True