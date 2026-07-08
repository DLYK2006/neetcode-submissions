class Node:
    def __init__(self):
        self.children={}
        self.isEnd=False
        self.index=0
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root=Node()
        self.board=board
        self.results=[]
        self.insert(words)
        self.words=words
        for a in range(len(board)):
            for b in range(len(board[a])):
                self.dfs(a,b,self.root)
        return self.results

    def insert(self,words):
            curr=self.root
            for i in range(len(words)):
                for ch in words[i]:
                    if ch not in curr.children:
                        curr.children[ch]=Node()
                    curr=curr.children[ch]
                curr.isEnd=True
                curr.index=i
                curr=self.root

    def dfs(self,a,b,node):
            
            if a==len(self.board) or a<0:
                return
            if b==len(self.board[a]) or b<0:
                return
            
            if self.board[a][b] in node.children:
                node=node.children[self.board[a][b]]
                if(node.isEnd) and node.index!=-1:
                    self.results.append(self.words[node.index])
                    node.index=-1
                temp=self.board[a][b]
                self.board[a][b]='#'
                self.dfs(a,b-1,node)
                self.dfs(a,b+1,node)
                self.dfs(a-1,b,node)
                self.dfs(a+1,b,node)
                self.board[a][b]=temp
            else:
                return