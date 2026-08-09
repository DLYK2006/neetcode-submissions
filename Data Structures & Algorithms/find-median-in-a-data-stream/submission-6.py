import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]


    def addNum(self, num: int) -> None:
        if self.minheap and num>=self.minheap[0]:
            heapq.heappush(self.minheap,num)
        elif self.maxheap and num<=-self.maxheap[0]:
            heapq.heappush(self.maxheap,-num)
        else:
            heapq.heappush(self.minheap,num)

        if len(self.minheap)>len(self.maxheap)+1:
            nums=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-nums)
        elif len(self.maxheap)>len(self.minheap):
            nums=heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap,-nums)

    def findMedian(self) -> float:
        if len(self.minheap)>len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.minheap[0]+(-1*self.maxheap[0]))/2
        