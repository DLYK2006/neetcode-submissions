import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency=defaultdict(int)
        heap=[]
        time=0
        queue=deque()
        for i in tasks:
            frequency[i]+=1
        
        for i in frequency:
            heapq.heappush(heap,(-frequency[i],i))

        while queue or heap:
            time+=1
            if heap:
                freq,task=heapq.heappop(heap)
                freq+=1
                if freq<0:
                    queue.append((freq,time+n))
            if queue:
                if queue[0][1]==time:
                    freq,cd=queue.popleft()
                    heapq.heappush(heap,(freq,task))
        return time 
    
        
        


