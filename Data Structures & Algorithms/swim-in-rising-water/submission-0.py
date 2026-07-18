import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[]
        heapq.heappush(heap,(grid[0][0],(0,0)))
        visit=set()

        while heap:
            time,(row,col)=heapq.heappop(heap)
            if(row,col)==(len(grid)-1,len(grid)-1):
                return time
            if (row,col) in visit:
                continue
            visit.add((row,col))
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in directions:
                nr,nc=row+dr,col+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[nr]) and (nr,nc) not in visit:
                    heapq.heappush(heap,(max(time,grid[nr][nc]),(nr,nc)))