from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words=defaultdict(list)
        for i in range(len(strs)):
            count=[0]*26
            for m in strs[i]:
                count[ord(m) - ord('a')] += 1
            words[tuple(count)].append(strs[i])
        
        result=[]
        for key,values in words.items():
            result.append(values)
            
        return result