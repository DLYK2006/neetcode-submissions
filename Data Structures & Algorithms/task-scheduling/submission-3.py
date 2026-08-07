from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        queue=deque()
        heap=[]
        frequency=defaultdict(int)
        for i in tasks:
            frequency[i]+=1
        
        for i in frequency:
            heapq.heappush(heap,(-frequency[i],i))
        
        while heap or queue:
            time+=1
            if heap:
                freq,letter=heapq.heappop(heap)
                freq+=1
                if freq<0:
                    queue.append((letter,time+n,freq))
            if queue and queue[0][1]==time:
                letter,cd,letterfreq=queue.popleft()
                heapq.heappush(heap,(letterfreq,letter))
        return time
