class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[nr]) and grid[nr][nc]=='1':
                    grid[nr][nc]='0'
                    dfs(nr,nc)
                    
        count=0
        for i in range(len(grid)):
            for m in range(len(grid[i])):
                if grid[i][m]=='1':
                    dfs(i,m)
                    count+=1
        
        return(count)

