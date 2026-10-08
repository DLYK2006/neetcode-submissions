from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency=defaultdict(int)
        for i in nums:
            frequency[i]+=1
        
        arr=list(frequency.items())
        result=[]
        heap=[]

        for number,frequency in arr:
            heapq.heappush(heap,(-frequency,number))
        
        while len(result)!=k:
            frequency,number=heapq.heappop(heap)
            result.append(number)
        
        return(result)
