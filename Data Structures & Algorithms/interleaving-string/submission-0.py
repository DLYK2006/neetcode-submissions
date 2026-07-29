class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        
        cache={}

        def helper(i,j):
            result=False
            if i+j==len(s3):
                return True
            k=i+j
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            if i<len(s1) and s1[i]==s3[k] :
                result=result or helper(i+1,j) 
            
            if j<len(s2) and s2[j]==s3[k]:
                result=result or helper(i,j+1) 

            cache[(i,j)]=result    
            return cache[(i,j)]
        
        return helper(0,0)