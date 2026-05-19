class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        frequency ={}
        highest=0
        answer=0

        while right < len(s):
            frequency[s[right]]=1+frequency.get(s[right],0)
            highest=max(highest,frequency[s[right]])
            if(right-left+1-highest>k):
                frequency[s[left]]-=1
                left+=1
            answer=max(answer,right-left+1)
            right+=1
        
        return answer