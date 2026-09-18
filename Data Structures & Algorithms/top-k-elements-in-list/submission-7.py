import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        heap=[]
        frequency=defaultdict(int)
        for i in nums:
            frequency[i]+=1
        for key,values in frequency.items():
            heapq.heappush(heap,-values)

        for i in range(k):
            temp=heapq.heappop(heap)*-1
            for key,values in frequency.items():
                if temp==values:
                    result.append(key)
                    del frequency[key]
                    break

        return result
