
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #adjacency list first
        #walkthrough the words till something is diff then append account for the length diff as well
        #use 2 sets dfs check for cycle
        graph={}
        for i in words:
            for char in i:
                graph[char]=set()

        for i in range(len(words)-1):  
            diff=False    #we use a flag to account for the length stuff
            for m in range(min(len(words[i]),len(words[i+1]))):
                if words[i][m]!=words[i+1][m]:
                    graph[words[i][m]].add(words[i+1][m])
                    diff=True
                    break                                #we only need to find 1 diff letter to map
            if not diff and len(words[i])>len(words[i+1]):
                return "" 
        print(graph)

        visitting=set()
        safe=set()
        result=[]
        def dfs(letter):
            if letter in visitting:
                return False
            if letter in safe:
                return True
            visitting.add(letter)
            for i in graph[letter]:
                print(i)
                if not dfs(i):
                    return False
            visitting.discard(letter)
            safe.add(letter)
            result.append(letter)
            return True
        
        for i in graph:
            if not dfs(i):
                return ""
        ans="".join(reversed(result))
        return ans

