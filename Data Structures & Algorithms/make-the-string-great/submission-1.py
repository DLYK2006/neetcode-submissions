class Solution:
    def makeGood(self, s: str) -> str:
        stack=deque()
        idx=0
        result=""

        while idx!=len(s):
            
            if stack and abs(ord(s[idx])-stack[-1])==32:
                stack.pop()
            else:
                stack.append(ord(s[idx]))
            idx+=1
        
        if len(stack)==0:
            return result
        else:
            while stack:
                result+=chr(stack[-1])
                stack.pop()
            return result[::-1]
        pass
