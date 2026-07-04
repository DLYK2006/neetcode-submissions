class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.words=word
        self.board=board
        self.rowl=len(board)
        self.coll=len(board[0])
        self.seen=set()
        for r in range(self.rowl):
            for c in range(self.coll):
                if self.dfs(r,c,0):
                    return True
        return False

    def dfs(self,r,c,i):
        if i==len(self.words):
            return True
        if r<0 or r>=self.rowl or c<0 or c>=self.coll:
            return False
        if (r,c) in self.seen or self.board[r][c]!=self.words[i]:
            return False
        
        self.seen.add((r,c))
        found=self.dfs(r+1,c,i+1)or self.dfs(r,c+1,i+1)or self.dfs(r-1,c,i+1)or self.dfs(r,c-1,i+1)
        self.seen.remove((r,c))
        return found