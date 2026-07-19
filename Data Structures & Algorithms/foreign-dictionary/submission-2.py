class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        self.adjacency=defaultdict(list)
        for a in words:
            for b in range(len(a)):
                if a[b] not in self.adjacency: 
                    self.adjacency[a[b]] = []
        for i in range(len(words)-1):
            m=0
            while m<len(words[i]):
        
                if words[i][m]==words[i+1][m]:
                    if len(words[i])>len(words[i+1]):
                        return ""
                    m+=1
                    continue
                else:
                    self.adjacency[words[i][m]].append(words[i+1][m])
                    break
                m+=1
        print(self.adjacency)
        visit=set()
        visiting=set()
        self.result=""
        for char, list_val in self.adjacency.items():
            print(char)
            if self.dfs(visit,visiting,char) is False:
                return ""
        self.result=self.result[::-1]
        return self.result
            

    def dfs(self,visit,visiting,node):
        if node in visiting:
            return False
        if node in visit:
            return 
        visiting.add(node)
        for i in range(len(self.adjacency[node])):
            if self.dfs(visit,visiting,self.adjacency[node][i]) is False:
                return ""
        visiting.remove(node)
        visit.add(node)
        self.result+=node
        
            
               

