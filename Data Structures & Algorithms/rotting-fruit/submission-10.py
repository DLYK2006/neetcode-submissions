class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        queue=deque()
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==2:
                    queue.append((i,m))
        
        while queue:
            print(time)
            time+=1
            for _ in range(len(queue)):    
                x,y=queue.popleft()
                directions=[(1,0),(-1,0),(0,1),(0,-1)]
                for dx,dy in directions:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                        queue.append((nx,ny))
                        grid[nx][ny]=2
            
        
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]==1:
                    return -1
        if time==0:
            return time
        else:
            return time-1
        