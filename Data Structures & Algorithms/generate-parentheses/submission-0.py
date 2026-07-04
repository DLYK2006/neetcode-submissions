class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result=[]
        current=""
        self.helper(n,0,0,current)
        return self.result

    def helper(self,n,grah,close,current):
        print(current)
        if grah==n and close==n:
            self.result.append(current)
            return 
        
        if grah<n:
            self.helper(n,grah+1,close,current+'(')

        if close<grah:
            self.helper(n,grah,close+1,current+')')