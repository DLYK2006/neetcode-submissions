class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache={}

        def helper(i,m):
            if (i,m) in cache:
                return cache[(i,m)]
            
            if i==len(text1):
                return 0
            if m==len(text2):
                return 0
            
            both,o1,o2=0,0,0


            if text1[i]==text2[m]:
                both=helper(i+1,m+1)+1
                cache[(i,m)]=both
            else:
                o1=helper(i+1,m)
                o2=helper(i,m+1)
                result=max(o1,o2)
                cache[(i,m)]=result
            
            return cache[(i,m)]

        return helper(0,0)