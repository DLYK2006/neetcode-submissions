from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph={c:set() for word in words for c in word}
        for i in range(len(words)-1):
            diff=False
            for m in range(min(len(words[i]),len(words[i+1]))):
                if words[i][m]!=words[i+1][m]:
                    graph[words[i][m]].add(words[i+1][m])
                    diff=True
                    break
            if not diff and len(words[i])>len(words[i+1]):
                return ""
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
                if not dfs(i):
                    return False
            visitting.discard(letter)
            safe.add(letter)
            result.append(letter)
            return True
        for i in graph:         
            if not dfs(i):
                return ""        
        return "".join(reversed(result))


            
