class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache={}

        def helper(i,j):
            if i==len(s) and j==len(p):
                return True
            elif i<len(s) and j==len(p):
                return False
            
            if (i,j) in cache:
                return cache[(i,j)]

            if i<len(s)and (s[i]==p[j] or p[j]=='.'):
                match=True
            else:
                match=False

            if j+1<len(p) and p[j+1]=='*':
                result=helper(i,j+2) or (match and helper(i+1,j))
            else:
                result=match and helper(i+1,j+1)

            cache[(i,j)]=result
            return result
        
        return helper(0,0)


