class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        cache={}
        hashset=set(words)

        def helper(word):
            if word in cache:
                return cache[word]
            
            for i in range(1,len(word)):
                start=word[:i]
                end=word[i:]

                if (start in hashset and end in hashset)or (start in hashset and helper(end)):
                    cache[word]=True
                    return True

            cache[word]=False
            return False
                
        results=[]
        for i in words:
            if helper(i):
                results.append(i)
        
        return results