class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board=board
        self.safe=set()
        grah=[]
        for a in range(len(self.board)):
            for b in range(len(self.board[a])):
                if self.board[a][b]=='O' and (a==0 or a==len(self.board)-1 or b==0 or b==len(self.board[0])-1) :
                    grah.append((a,b))
                    self.safe.add((a,b))
        
        for r,c in grah:
            self.dfs(r,c)

        print(self.safe)
        for a in range(len(self.board)):
            for b in range(len(self.board[a])):
                if self.board[a][b]=='#' or ((a,b)) in self.safe:
                    self.board[a][b]='O'
                else:
                    self.board[a][b]='X'
        print(self.board)
                    
    def dfs(self,r,c):
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            nr,nc=r+dr,c+dc
            if 0<=nr<len(self.board) and 0<=nc<len(self.board[0]) and self.board[nr][nc]=='O':
                self.safe.add((nr,nc))
                self.board[nr][nc]='#'
                self.dfs(nr,nc)

