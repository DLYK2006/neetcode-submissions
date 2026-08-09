class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        fresh=0
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==2:
                    queue.append((i,m))
                elif grid[i][m]==1:
                    fresh+=1
        time=0
        if fresh==0:
            return 0

        while queue and fresh>0:
            time+=1
            for i in range(len(queue)):
                r,c=queue.popleft()
                direction=[(0,1),(0,-1),(1,0),(-1,0)]
                for dr,dc in direction:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[nr]) and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=0
                        queue.append((nr,nc))
            

        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==1:
                    return -1
        
        return time

        
