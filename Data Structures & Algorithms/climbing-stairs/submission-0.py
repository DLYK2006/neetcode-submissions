class Solution:
    def climbStairs(self, n: int) -> int:
        self.grah=[-1]*n
        self.dfs(0,n)
        return self.grah[0]
        

    def dfs(self,i,n):
        if i==n:
            return 1
        if i>n:
            return 0 
         
        if self.grah[i]!=-1:
            return self.grah[i]
        
        self.grah[i]=(self.dfs(i+1,n)+self.dfs(i+2,n))
        return self.grah[i]
    