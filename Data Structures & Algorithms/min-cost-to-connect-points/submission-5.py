import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap=[]
        time=0
        visit=set()
        heapq.heappush(heap,(0,0))

        while len(visit)<len(points):
            cost,node=heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            time+=cost
            for nodes in range(len(points)):
                if nodes not in visit:
                    cost=abs(points[node][0]-points[nodes][0])+abs(points[node][1]-points[nodes][1])
                    heapq.heappush(heap,(cost,nodes))
        return time