class Solution:
    def isValid(self, s: str) -> bool:
        punc={}
        start=["(","{","["]
        end=[")","}","]"]

        for i in range(len(start)):
            punc[start[i]]=end[i]

        print(punc)
        stack=deque()

        for i in s:
            if i in start:
                stack.append(i)
            elif i in end:
                print(stack)
                if len(stack)>0 and i==punc[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        if len(stack)==0:
            return True
        else:
            return False



