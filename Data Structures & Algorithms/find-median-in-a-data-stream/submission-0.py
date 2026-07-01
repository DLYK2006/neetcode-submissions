import heapq

class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        

    def addNum(self, num: int) -> None:
        grah=0
        heapq.heappush(self.maxheap,-num)
        grah=heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,-grah)
        if len(self.minheap)>len(self.maxheap):
            grah=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,-grah)
        print(self.minheap)
        print(self.maxheap)

    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (self.minheap[0]+(-1*self.maxheap[0]))/2
        else:
            return -1*self.maxheap[0]