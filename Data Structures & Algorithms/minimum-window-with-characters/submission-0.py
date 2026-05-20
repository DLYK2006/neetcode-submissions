class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        right=0
        have=0
        need={}
        windowcount={}
        answer=""
        answerLen = 1000

        for i in range(len(t)):
            need[t[i]]=1+need.get(t[i],0)
        
        needCount=len(need)

        while right<len(s):
            print(windowcount)
            windowcount[s[right]]=1+windowcount.get(s[right],0)
            if(s[right] in need and windowcount[s[right]] == need[s[right]]):
                have+=1
            right+=1

            while have==needCount:
                if right - left < answerLen:
                    answer = s[left:right]
                    answerLen = right - left
                windowcount[s[left]]-=1
                if(s[left] in need and windowcount[s[left]] < need[s[left]]):
                    have-=1
                if(windowcount[s[left]]==0):
                    del windowcount[s[left]]
                left+=1
        
        return answer
        
        