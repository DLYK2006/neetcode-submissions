
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph={}
        for i in words:
            for char in i:
                graph[char]=set()
        for i in range(len(words)-1):
            diff=False
            for m in range(min(len(words[i]),len(words[i+1]))):
                if words[i][m]!=words[i+1][m]:
                    graph[words[i][m]].add(words[i+1][m])
                    diff=True
                    break
            if len(words[i])>len(words[i+1]) and diff is False:
                return ""
        
        visit=set()
        safe=set()
        result=[]

        def dfs(letter):
            if letter in visit:
                return False
            if letter in safe:
                return True
            
            visit.add(letter)
            for i in graph[letter]:
                if not dfs(i):
                    return False
            visit.discard(letter)
            safe.add(letter)
            result.append(letter)
            return True
        
        for i in graph:
            if dfs(i) is False:
                return ""
        ans=''.join(reversed(result))
        return ans
