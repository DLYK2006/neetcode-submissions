class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result=[]
        self.numbers=nums
        current=[]
        self.helper(0,target,current)
        return self.result

    def helper(self,i,target,current):
        if target==0:
            self.result.append(current.copy())
            return current
            
        elif i==len(self.numbers) or target<0:
            return current
            
        current.append(self.numbers[i])
        self.helper(i,target-self.numbers[i],current)
        current.pop()
        self.helper(i+1,target,current)