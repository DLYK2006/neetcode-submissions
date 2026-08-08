from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph=defaultdict(list)
        for i in wordList:
            for m in range(len(i)):
                new=i[:m]+'*'+i[m+1:]
                graph[new].append(i)
        self.count=1
        queue=deque()
        queue.append(beginWord)
        visit=set()

        def bfs():
            while queue:
                for i in range(len(queue)):
                    word=queue.popleft()
                    if word in visit:
                        continue
                    if word==endWord:
                        return True
                    visit.add(word)
                    for m in range(len(word)):
                        new=word[:m]+'*'+word[m+1:]
                        for w in graph[new]:
                            if w not in visit:
                                queue.append(w)
                self.count+=1
            return False
        
        if bfs():
            return(self.count)
        else:
            return 0
        
        
