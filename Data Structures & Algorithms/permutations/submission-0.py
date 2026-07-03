class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        current=[]
        self.result=[]
        decisions=[]
        for i in range(len(nums)):
            decisions.append(False)
        
        self.helper(current,decisions,nums)
        return self.result

    def helper(self,current,decisions,nums):
        if len(current)==len(nums):
            self.result.append(current.copy())
            return
        
        for a in range(len(nums)):
            if(decisions[a])==False:
                current.append(nums[a])
                decisions[a]=True
                self.helper(current,decisions,nums)
                current.pop()
                decisions[a]=False
                       