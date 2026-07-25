class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache={}

        def helper(i,j):
            if (i,j)==(m-1,n-1):
                return 1
            if i==m or j==n:
                return 0
            if (i,j)in cache:
                return cache[(i,j)]
            
            down=helper(i+1,j)
            right=helper(i,j+1)

            result=down+right
            cache[(i,j)]=result
            return cache[(i,j)]
        
        return helper(0,0)
        
        
        