import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in range(len(stones)):
            heapq.heappush(heap,-stones[i])
        
        while len(heap)>1:
            stone1=-heap[0]
            heapq.heappop(heap)
            stone2=-heap[0]
            if(stone1==stone2):
                heapq.heappop(heap)
            elif(stone1>stone2):
                heapq.heappop(heap)
                new=stone1-stone2
                heapq.heappush(heap,-new)
            
        if len(heap)==1:
            return -heap[0]
        else:
            return 0
            