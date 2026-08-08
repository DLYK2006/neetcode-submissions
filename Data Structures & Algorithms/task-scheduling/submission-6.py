from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        graph=defaultdict(int)
        time=0
        queue=deque()
        for i in tasks:
            graph[i]+=1
        
        heap=[]
        for i in graph:
            heapq.heappush(heap,(-graph[i]))
        
        while heap or queue:
            time+=1
            if heap:
                freq=heapq.heappop(heap)
                freq+=1
                if freq<0:
                    queue.append((freq,time+n))
            
            if queue and time==queue[0][1]:
                letterfreq,cd=queue.popleft()
                heapq.heappush(heap,(letterfreq))
        
        return time
