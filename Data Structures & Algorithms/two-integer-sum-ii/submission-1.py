class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        front=0
        back=-1
        results=[]

        while (numbers[front]+numbers[back]!=target):
            if numbers[front]+numbers[back]>target:
                back-=1
                continue
            elif(numbers[front]+numbers[back]<target):
                front+=1
                continue
            elif(numbers[front]+numbers[back]==target):
                break
        results.append(front+1)
        results.append(back+len(numbers)+1) 
        return results