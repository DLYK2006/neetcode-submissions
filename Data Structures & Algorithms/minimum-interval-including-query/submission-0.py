import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals=sorted(intervals)
        sorted_queries = sorted([(q, idx) for idx, q in enumerate(queries)])
        print(sorted_queries)
        i=0
        a=0
        heap=[]
        result=[-1]*len(queries)

        while i<len(sorted_queries):
            idx = sorted_queries[i][1]
            while a<len(intervals) and intervals[a][0]<=sorted_queries[i][0]:
                heapq.heappush(heap,(intervals[a][1]-intervals[a][0]+1,intervals[a][1]))
                a+=1    
            while heap and heap[0][1]<sorted_queries[i][0]:
                heapq.heappop(heap)
            if heap:
                result[idx]=heap[0][0]
            i+=1
        
        return result