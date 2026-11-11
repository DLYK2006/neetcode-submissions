class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==1:
            return s
        
        ans=""
        left=0
        right=0
        
        while right!=len(s):
            if s[right]!=" ":
                right+=1  

            else:
                for i in range(right-1,left-1,-1):
                    ans+=s[i]
                right+=1
                left=right
                ans+=" "
        for i in range(right-1,left-1,-1):
            ans+=s[i]
     
        return (ans)

        pass