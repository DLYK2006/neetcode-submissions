class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]


        for i in range (len(temperatures)):
            print("stack:" ,stack)
            print("result", result)
            if i==0:
                stack.append(i)
                continue
            while stack and temperatures[i]>temperatures[stack[-1]]:
                result[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        
        difference=len(temperatures)-len(result)


        return result
