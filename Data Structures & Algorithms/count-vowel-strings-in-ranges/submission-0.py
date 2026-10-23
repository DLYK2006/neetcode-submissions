class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels=['a','e','i','o','u']
        result=[]

        for l,r in queries:
            answer=0
            for i in range(l,r+1):
                if (words[i][0] in vowels) and (words[i][-1] in vowels):
                    answer+=1
            result.append(answer)
    
        return result
        

