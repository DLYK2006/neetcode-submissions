import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}
        for i in range(1,n+1):
            graph[i]=[]
        for a,b,c in times:
            graph[a].append((c,b))
        
        dist=[float('inf')]*n
        dist[k-1]=0
        heap=[]
        heapq.heappush(heap,(0,k)) 
        while heap:
            distance,target=heapq.heappop(heap)
            for cost,node in graph[target]:
                if distance+cost<dist[node-1]:
                    dist[node-1]=distance+cost
                    heapq.heappush(heap,(distance+cost,node))
        if max(dist)==float('inf'):
            return -1
        else:
            return max(dist) 