class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights=heights
        atlantic=set()
        pacific=set()
        for i in range(len(heights)):
            for m in range(len(heights[i])):
                if m==0 or i==0:
                    pacific.add((i,m))
                if m==len(heights[i])-1 or i==len(heights)-1:
                    atlantic.add((i,m))
        seen1=set()
        seen2=set()
        for i,m in pacific:
            self.dfs(i,m,seen2)
        for i,m in atlantic:
            self.dfs(i,m,seen1)
        result=[]
        for i in range(len(heights)):
            for m in range(len(heights[i])):
                if (i,m) in seen1 and (i,m) in seen2:
                    result.append([i,m])

        return result

    def dfs(self,r,c,seen):
        if (r,c)in seen:
            return
        else:
            seen.add((r,c))
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in directions:
            nr=r+dr
            nc=c+dc
            if 0<=nr<len(self.heights) and 0<=nc<len(self.heights[nr]) and self.heights[nr][nc]>=self.heights[r][c]:
                self.dfs(nr,nc,seen)
