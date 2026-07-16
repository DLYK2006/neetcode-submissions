class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                patterns[pattern].append(word)
        queue=deque()
        queue.append(beginWord)
        visit=set()
        level=1
        while queue:
            for b in range(len(queue)):    
                popped=queue.popleft()
                if popped==endWord:
                    return level
                for i in range(len(popped)):
                    pattern = popped[:i] + '*' + popped[i+1:]
                    for a in range(len(patterns[pattern])):
                        if patterns[pattern][a] not in visit:
                            queue.append(patterns[pattern][a])
                            visit.add(patterns[pattern][a])
            level+=1     
        return 0