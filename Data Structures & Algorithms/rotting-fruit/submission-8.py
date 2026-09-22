class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.queue=deque()
        count=0
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==2:
                    self.queue.append((i,m))
        
        while self.queue:
            count+=1
            print(self.queue)
            print(count)
            for _ in range(len(self.queue)):
                i,m=self.queue.popleft()
                directions=[(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    nr=i+dr
                    nc=m+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                        self.queue.append((nr,nc))
                        grid[nr][nc]=2
            
        
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==1:
                    return -1
        if count==0:
            return count
        else:
            return count-1

        
        
