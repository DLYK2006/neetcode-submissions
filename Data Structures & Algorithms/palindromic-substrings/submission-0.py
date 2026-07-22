class Solution:
    def countSubstrings(self, s: str) -> int:
        self.palindromes=len(s)

        def expand(b,f):
            while b>=0 and f<len(s) and s[b]==s[f]:
                self.palindromes+=1
                b-=1
                f+=1
            
        for i in range(len(s)):
            expand(i-1,i+1)
            expand(i,i+1)
        return self.palindromes
            
        