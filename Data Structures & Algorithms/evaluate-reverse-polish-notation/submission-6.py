class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=["+","-","*","/"]

        for i in range(len(tokens)):
            print(stack)
            result=0
            if(tokens[i] not in operations):
                stack.append(int(tokens[i]))
            elif(tokens[i] in operations):
                popped1=int(stack.pop())
                popped2=int(stack.pop())

                match operations.index(tokens[i]):
                    case 0:
                        result=popped2+popped1
                    case 1:
                        result=popped2-popped1
                    case 2:
                        result=popped2*popped1
                    case 3:
                        result=popped2/popped1

                stack.append(int(result))
        return stack[-1]

                
                