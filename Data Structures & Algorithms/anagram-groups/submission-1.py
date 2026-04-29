class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary={}
        for i in strs:
            temp="".join(sorted(i))
            if temp not in dictionary:
                dictionary[temp]=[]
            dictionary[temp].append(i)
        output=list(dictionary.values())
        return output