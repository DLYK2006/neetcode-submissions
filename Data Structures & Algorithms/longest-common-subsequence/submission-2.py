class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache={}

        def helper(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==len(text1):
                return 0
            if j==len(text2):
                return 0
            
            together,nah1,nah2=0,0,0

            if text1[i]==text2[j]:
                together=1+helper(i+1,j+1)
                cache[(i,j)]=together
            else:
                nah1=helper(i,j+1)
                nah2=helper(i+1,j)
                result=max(nah1,nah2)
                cache[(i,j)]=result
            return cache[(i,j)]
        
        return (helper(0,0))

