class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights=heights
        pacific=set()
        visited=set()
        atlantic=set()
        result=[]
        for a in range(len(heights)):
            for b in range(len(heights[a])):
                if a==0 or b==0:
                    pacific.add((a,b))

                if a==len(heights)-1 or b==len(heights[a])-1:
                    atlantic.add((a,b))
        for r,c in pacific:
            self.dfs(r,c,visited)
        visited2=set()
        for r,c in atlantic:
            self.dfs(r,c,visited2)

        for a in range(len(heights)):
            for b in range(len(heights[a])):
                if (a,b) in visited and (a,b) in visited2:
                    result.append([a,b])
                    
        return result

    def dfs(self,r,c,visited):
        visited.add((r,c))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for a,b in directions:
            nr,nc = a+ r, b+ c
            if 0<=nr<len(self.heights) and 0<=nc<len(self.heights[0]) and (nr,nc) not in visited and self.heights[nr][nc]>=self.heights[r][c]:
                self.dfs(nr,nc,visited)
