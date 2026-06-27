import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        distance=0
        xcoord=0
        ycoord=0
        for x,y in points:
            xcoord=(x-0)**2
            ycoord=(y-0)**2
            print(xcoord)
            print(ycoord)
            distance=math.sqrt(xcoord+ycoord)
            heapq.heappush(heap,(-distance,[x,y]))
        print(heap)
        while(len(heap)>k):
            heapq.heappop(heap)
        print(heap)
        return [pair[1] for pair in heap]