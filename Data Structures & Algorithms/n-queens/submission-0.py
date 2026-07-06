class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results=[]
        current=[]
        for i in range(n):
            current.append(['.']*n)

        self.n=n
        self.helper(current,0)
        return self.results

    
    def helper(self,current,r):

        if r==self.n:
            self.results.append([''.join(r) for r in current])
            return 

        for c in range(self.n):
            if(self.checker(current,r,c)):
                current[r][c]='Q'
                self.helper(current,r+1)
                current[r][c]='.'

    def checker(self,current,r,c):
        i = r-1
        while i>=0:
            if current[i][c]=='Q':
                return False
            i-=1

        i,j=r-1,c-1
        while i>= 0 and j>=0:
            if current[i][j]=='Q':
                return False
            i-=1
            j-=1

        i,j=r-1,c+1
        while i>= 0 and j<self.n:
            if current[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True
