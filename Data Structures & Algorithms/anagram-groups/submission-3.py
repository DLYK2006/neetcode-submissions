
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)

        for i in range(len(strs)):
            letters=[0]*26
            for m in strs[i]:
                letters[ord(m)-ord('a')]+=1
            words[tuple(letters)].append(strs[i])

        return list(words.values())