import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit=set()
        total=0
        heap=[]
        heapq.heappush(heap,(0,0))

        while len(visit)<len(points):           
            cost,node=heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            total+=cost
            for j in range(len(points)):
                if j not in visit:
                    cost=abs(points[node][0]-points[j][0])+abs(points[node][1]-points[j][1])
                    heapq.heappush(heap,(cost,j))
        
        return total