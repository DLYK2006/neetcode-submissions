import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        heap=[]
        for a,b,c in times:
            if a not in graph:
                graph[a]=[]
            graph[a].append((b,c))
        visit=set()

        heapq.heappush(heap,(0,k))
        distance={}
        while heap:
            dist,node=heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            distance[node]=dist
            for target,weight in graph[node]:
                if target not in visit:
                    heapq.heappush(heap,(dist+weight,target))
        
        if len(distance)<n:
            return -1
        return max(distance.values())