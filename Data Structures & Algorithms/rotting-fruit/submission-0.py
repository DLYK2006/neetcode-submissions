class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        fresh=0
        queue=deque()
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b]==1:
                    fresh+=1
                if grid[a][b]==2:
                    queue.append((a,b))
        grah=fresh

        while queue:
            if(grah<fresh):
                fresh=grah
                time+=1
            for _ in range(len(queue)):
                a,b=queue.popleft()
                row,col=len(grid),len(grid[0])
                directions=[(-1,0),(1,0),(0,-1),(0,1)]
                for r,c in directions:
                    nr,nc=a+r,b+c
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        grah-=1
                        queue.append((nr,nc))

        if fresh==0:
            return time
        else:
            return -1