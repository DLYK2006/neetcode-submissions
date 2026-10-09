import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequency=defaultdict(int)
        for i in tasks:
            frequency[i]+=1
        
        heap=[]
        time=0
        queue=deque()

        for m in frequency:
            heapq.heappush(heap,-frequency[m])

        while heap or queue:
            time+=1
            if heap:
                freq=heapq.heappop(heap)
                freq=(freq*-1)-1
                if freq>0:
                    queue.append((freq,time+n))
            while queue and queue[0][1]==time:
                freq,cooldown=queue.popleft()
                heapq.heappush(heap,(-freq))
        
        return (time)