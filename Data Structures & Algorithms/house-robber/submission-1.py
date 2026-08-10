class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        amount=0
    
        def helper(i):
            if i in cache:
                return cache[i]
            if i>=len(nums):
                return 0        
            amount=max(nums[i]+helper(i+2),helper(i+1))

            cache[i]=amount
            return cache[i]
        
        return helper(0)
        
            
            