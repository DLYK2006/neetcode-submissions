class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum=0
        self.area=0
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if grid[a][b]==1:
                    self.dfs(grid,a,b)
                maximum=max(maximum,self.area)
                self.area=0
        return maximum

    def dfs(self,grid,a,b):

        if a<0 or a>=len(grid):
            return
        if b<0 or b>=len(grid[a]):
            return
        if(grid[a][b]==1):
            self.area+=1
            grid[a][b]=0
            self.dfs(grid,a,b-1)
            self.dfs(grid,a,b+1)
            self.dfs(grid,a-1,b)
            self.dfs(grid,a+1,b)

        