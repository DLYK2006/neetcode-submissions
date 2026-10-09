import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]

        for i in points:
            x=i[0]
            y=i[1]

            distance=pow(((x - 0)**2 + (y - 0)**2),0.5)
            
            heapq.heappush(heap,(distance,i))
        
        result=[]
        print(heap)

        while len(result)!=k:
            distance,i=heapq.heappop(heap)
            result.append(i)
        
        return result