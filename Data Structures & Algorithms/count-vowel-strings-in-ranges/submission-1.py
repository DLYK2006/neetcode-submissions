class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels=set("aeiou")
        result=[0]*len(queries)
        prefix=[0]*(len(words)+1)
        prev=0

        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prev+=1
            prefix[i+1]=prev
        
        for i,q in enumerate(queries):
            l,r=q
            result[i]=prefix[r+1]-prefix[l]
        
        return result
            