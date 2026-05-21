class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        if(len(s)<2):
            return False
        print(pairs)
        
        for i in range(len(s)):
            if(s[i] in pairs.values()):
                stack.append(s[i])
                continue
            else:
                print(stack)
                if(len(stack)==0):
                    return False
                if(pairs[s[i]]!=stack[-1]):
                    return False
                stack.pop()
        if(len(stack)==0):
            return True
        else:
            return False