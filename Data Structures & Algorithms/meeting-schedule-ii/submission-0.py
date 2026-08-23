"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starting=[]
        ending=[]
        for i in intervals:
            starting.append(i.start)
            ending.append(i.end)
        
        starting=sorted(starting)
        ending=sorted(ending)
        count=0
        result=0
        s=0
        e=0
        while s<len(starting):
            if starting[s]<ending[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            result=max(count,result)
        
        return result