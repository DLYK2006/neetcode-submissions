class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts={}

        for char in s:
            counts[char]=counts.get(char,0)+1
        
        for char in t:
            counts[char]=counts.get(char,0)-1
        
        for value in counts.values():
            if value != 0:
                return False
        
        return True