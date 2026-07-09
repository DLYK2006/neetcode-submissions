class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.groups=0
        for a in range(len(grid)):
            for b in range(len(grid[a])):
                if(grid[a][b]=="1"):
                    self.dfs(grid,a,b)
                    self.groups+=1
        
        return self.groups

    def dfs(self,grid,a,b):
        if a<0 or a>=len(grid):
            return
        if b<0 or b>=len(grid[a]):
            return
                    
        if(grid[a][b]=="1"):
            grid[a][b]=0
            self.dfs(grid,a,b-1)
            self.dfs(grid,a,b+1)
            self.dfs(grid,a+1,b)
            self.dfs(grid,a-1,b)