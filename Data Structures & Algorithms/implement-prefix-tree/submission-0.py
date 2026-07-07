class Node:
    def __init__(self):
        self.children={}
        self.isEnd= False


class PrefixTree:

    def __init__(self):
        self.root=Node()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for i in word:
            if i not in curr.children:
                curr.children[i]=Node()
            curr=curr.children[i]
        curr.isEnd=True

    def search(self, word: str) -> bool:
        curr=self.root
        for i in word:
            if i in curr.children:
                curr=curr.children[i]
            else:
                return False
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i in prefix:
            if i in curr.children:
                curr=curr.children[i]
            else:
                return False
        return True
