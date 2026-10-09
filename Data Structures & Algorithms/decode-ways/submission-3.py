class Solution:
    def numDecodings(self, s: str) -> int:
        cache={}

        def helper(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            if i in cache:
                return cache[i]
            
            result=helper(i+1)

            if  (i+1<len(s)) and ((s[i]=='1' and '0'<=s[i+1]<='9') or (s[i]=='2' and ('0'<=s[i+1]<='6'))):
                result+=helper(i+2)
            
            cache[i]=result
            return result
        
        return (helper(0))
            
