class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen=0
        res=0
        

        def helper(b,f):
            while b>=0 and f<len(s) and s[b]==s[f]:
                b-=1
                f+=1
            return f-b-1,b+1

        for i in range(len(s)):
            temp1,temp2=helper(i,i)
            resLen=max(resLen,temp1)
            if resLen==temp1:
                res=temp2
            temp1,temp2=helper(i,i+1)
            resLen=max(resLen,temp1)
            if resLen==temp1:
                res=temp2
        
        return s[res:res+resLen]
        

