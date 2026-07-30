class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}

        def helper(i,j):

            if j==len(t):
                return 1

            if i==len(s):
                return 0            

            if (i,j) in cache:
                return cache[(i,j)]
            include=0

            if s[i]==t[j]:
                include=helper(i+1,j+1)
            exclude=helper(i+1,j)
            
            result=include+exclude
            cache[(i,j)]=result
            return cache[(i,j)]
        
        return helper(0,0)
        