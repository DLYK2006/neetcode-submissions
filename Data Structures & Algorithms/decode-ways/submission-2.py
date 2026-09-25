class Solution:
    def numDecodings(self, s: str) -> int:
        cache={}

        def helper(i):
            if i==len(s):
                return 1

            if i in cache:
                return cache[i]

            if s[i]=='0':
                return 0
            
            result=helper(i+1)

            if i+1<len(s) and (s[i]=='1' or s[i]=='2' and s[i+1] in '0123456'):
                result+=helper(i+2)
             
            cache[i]=result
            return result
        
        return helper(0)

