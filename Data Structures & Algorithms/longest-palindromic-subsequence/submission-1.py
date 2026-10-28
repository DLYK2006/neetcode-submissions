class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache={}

        def helper(i,m):
            if (i,m) in cache:
                return cache[(i,m)]
            if i==m:
                return 1
            if i>m:
                return 0
            result=0
            if s[i]==s[m]:
                result= 2+helper(i+1,m-1)
            else:
                result=max(helper(i+1,m),helper(i,m-1))
            cache[(i,m)]=result
            return result
            
            
        return helper(0,len(s)-1)
        
        