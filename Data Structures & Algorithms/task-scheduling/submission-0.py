import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts={}
        heap=[]
        queue=deque()
        time=0

        for i in tasks:
            counts[i]=counts.get(i,0)+1
        
        for i in counts:
            heapq.heappush(heap,-counts[i])
        
        while heap or queue:
            time+=1
            if heap:
                task=heapq.heappop(heap)+1
                if task!= 0:
                    queue.append([task,time+n])
            if queue and queue[0][1]==time:
                heapq.heappush(heap,queue[0][0])
                queue.popleft()
        return time