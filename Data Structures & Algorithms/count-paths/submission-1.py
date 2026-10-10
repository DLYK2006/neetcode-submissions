class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache={}

        def helper(x,y):
            if (x,y) in cache:
                return cache[(x,y)]
            if x==m or y==n:
                return 0
            if x==m-1 and y==n-1:
                return 1
            result=0
            result=helper(x+1,y)+helper(x,y+1)
            cache[(x,y)]=result
            return result
        
        return (helper(0,0))
            