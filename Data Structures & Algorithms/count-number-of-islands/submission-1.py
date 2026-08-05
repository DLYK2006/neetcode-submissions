class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid=grid
        count=0
        for i in range(len(self.grid)):
            for m in range(len(self.grid[i])):
                if self.grid[i][m]=='1':
                    self.dfs(i,m)
                    count+=1
        return count

    def dfs(self,r,c):
        self.grid[r][c]='0'
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in directions:
            nr=r+dr
            nc=c+dc
            if 0<=nr<len(self.grid) and 0<=nc<len(self.grid[nr]) and self.grid[nr][nc]=='1':
                self.dfs(nr,nc)               
            else:
                continue


