class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexes={}
        result=[]
        for i in range(-1,-len(s)-1,-1):
            if s[i] not in indexes:
                indexes[s[i]]=i+len(s)
        
        start=0
        end=0
        for i,char in enumerate(s):
            end=max(end,indexes[char])

            if i==end:
                result.append(end-start+1)
                start=i+1
        return result

            
