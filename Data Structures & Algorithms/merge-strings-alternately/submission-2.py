class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        ptr=0
        ptr2=0
        while ptr<len(word1) or ptr2<len(word2):
            if ptr<len(word1):
                new+=word1[ptr]
                ptr+=1
                
            if  ptr2<len(word2):
                new+=word2[ptr2]
                ptr2+=1
        
        return new
            