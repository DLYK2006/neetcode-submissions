from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph=defaultdict(list)
        for i in (wordList):
            for m in range(len(i)):
                pattern=i[:m]+'*'+i[m+1:]
                graph[pattern].append(i)
        
        visit=set()
        queue=deque()
        queue.append(beginWord)
        self.count=1
        print(graph)
        def bfs():
            while queue:
                for i in range(len(queue)):
                    word=queue.popleft()
                    if word==endWord:
                        return True
                    visit.add(word)
                    for m in range(len(word)):
                        pattern=word[:m]+'*'+word[m+1:]
                        for words in graph[pattern]:
                            if words in visit:
                                continue
                            queue.append(words)
                self.count+=1
        if not bfs():
            return 0
        else:
            return self.count

        
        