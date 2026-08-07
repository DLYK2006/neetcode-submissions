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
        heap=[(0,k)]
        
        while heap:
            time , edge = heapq.heappop(heap)
            if time>dist[edge-1]:
                continue
            for cost,edges in graph[edge]:
                if time+cost<dist[edges-1]:
                    dist[edges-1]=time+cost
                    heapq.heappush(heap,(dist[edges-1],edges))
        print(dist)
        result=max(dist)
        if result==float('inf'):
            return -1
        else:
            return result
