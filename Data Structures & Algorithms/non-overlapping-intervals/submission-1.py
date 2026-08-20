class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals)
        count=0
        if intervals:
            prevEnd=intervals[0][1]
        
        for i in range(1,len(intervals)):
            if prevEnd<=intervals[i][0]:
                prevEnd=intervals[i][1]
                continue
            else:
                prevEnd=min(prevEnd,intervals[i][1])
                count+=1
        return count