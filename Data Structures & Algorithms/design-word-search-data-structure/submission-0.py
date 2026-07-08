class Node:
    def __init__(self):
        self.children={}
        self.isEnd= False

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        curr=self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=Node()
            curr=curr.children[ch]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self.root
        return self.dfs(word,curr,0)

    def dfs(self,word,node,i):
        if i==len(word):
            return node.isEnd
        if word[i]!='.':
            if word[i] not in node.children:
                return False
            else:
                return self.dfs(word,node.children[word[i]],i+1)
        else:
            for child in node.children.values():
                if(self.dfs(word,child,i+1)):
                    return True
            return False

