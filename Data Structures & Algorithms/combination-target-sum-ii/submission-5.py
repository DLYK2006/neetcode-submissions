class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums=sorted(candidates)
        self.results=[]
        current=[]
        self.helper(0,target,current)
        return self.results

    def helper(self,i,target,current):
        if target==0:
            self.results.append(current.copy())
            return 
        elif target<0 or i==len(self.nums):
            return current
        
        for a in range (i,len(self.nums)):
            if(self.nums[a]==self.nums[a-1])and a>i:
                continue
            current.append(self.nums[a])
            self.helper(a+1,target-self.nums[a],current)
            current.pop()
        