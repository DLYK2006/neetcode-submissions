class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cache={}
        current=0

        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            
            if r==len(points):
                return 0

            maxn=float('-inf')
            for i in range(len(points[0])):
                if c==-1:
                    penalty=0
                else:
                    penalty=abs(c-i)
                gain = points[r][i]-penalty+dfs(r+1,i)
                maxn=max(maxn,gain)

            cache[(r,c)]=maxn
            return maxn
        
        return dfs(0,-1)
                


            

            
            