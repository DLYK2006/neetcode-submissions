class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        result=[]
        while i<len(intervals):
            if result and result[-1][1]>=intervals[i][0]:
                intervals[i][0]=min(result[-1][0],intervals[i][0])
                intervals[i][1]=max(result[-1][1],intervals[i][1])
                result.pop()
                result.append(intervals[i])
            else:
                result.append(intervals[i])
            i+=1
        return (result)