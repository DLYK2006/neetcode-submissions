import heapq
class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        if not self.minheap or num>self.minheap[0]:
            heapq.heappush(self.minheap,num)
        else:
            heapq.heappush(self.maxheap,-num)
        
        if len(self.minheap)>len(self.maxheap)+1:
            nums=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-nums)
        elif len(self.maxheap)>len(self.minheap)+1:
            nums=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-nums)
    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            median=((-1*self.maxheap[0])+self.minheap[0])/2
        elif len(self.minheap)>len(self.maxheap):
            median=self.minheap[0]
        else:
            median=-self.maxheap[0]
        return median
        
        