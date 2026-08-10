from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        for i in wordList:
            for m in range(len(i)):
                patterns = i[:m] + "*" + i[m + 1 :]
                graph[patterns].append(i)

        queue = deque()
        self.count = 1
        visit = set()
        visit.add(beginWord)
        queue.append(beginWord)

        def bfs():
            while queue:
                for i in range(len(queue)):
                    word = queue.popleft()
                    if word == endWord:
                        return True
                    for m in range(len(word)):
                        patterns = word[:m] + "*" + word[m + 1 :]
                        for words in graph[patterns]:
                            if words not in visit:
                                queue.append(words)
                            visit.add(words)
                self.count += 1

            return False

        if bfs():
            return self.count
        else:
            return 0
