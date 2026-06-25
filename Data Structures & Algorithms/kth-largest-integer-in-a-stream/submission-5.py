import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.length=k
        for i in range(len(nums)):
            heapq.heappush(self.heap,nums[i])
        
        while len(self.heap)>self.length:
            heapq.heappop(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
    
        heapq.heappush(self.heap,val)
        
        while len(self.heap)>self.length:
            heapq.heappop(self.heap)
        
        return self.heap[0]