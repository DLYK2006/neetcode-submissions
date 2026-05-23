class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        timeTakenS=[]
        stack=[]

        for position,speed in cars:
            timeTakenS.append((target-position)/speed)
        
        print(timeTakenS)
        
        stack.append(timeTakenS[0])
        for i in range(len(timeTakenS)):
            if(timeTakenS[i]>stack[-1]):
                stack.append(timeTakenS[i])
            
                        
        return len(stack)