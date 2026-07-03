class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums=sorted(nums)
        current=[]
        self.result=[]
        self.helper(0,current)
        return self.result

    
    def helper(self,index,current):
        self.result.append(current.copy())
        
        for i in range(index,len(self.nums)):
            if i>index and self.nums[i]==self.nums[i-1]:
                continue
            current.append(self.nums[i])
            self.helper(i+1,current)
            current.pop()
        