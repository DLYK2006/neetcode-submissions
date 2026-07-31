class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache={}

        def helper(i,j):
            if i==len(word1):
                return len(word2)-j
            
            if j==len(word2):
                return len(word1)-i
            
            if (i,j) in cache:
                return cache[(i,j)]

            if word1[i]==word2[j]:
                result=helper(i+1,j+1)
            else:
                insert=helper(i,j+1)
                delete=helper(i+1,j)
                replace=helper(i+1,j+1)
                result=min(insert,delete,replace)+1

            
            cache[(i,j)]=result
            return cache[(i,j)]
        
        return helper(0,0)