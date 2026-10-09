class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}

        def helper(i):
            if i>=len(nums):
                return 0
            
            if i in cache:
                return cache[i]
            
            buy=nums[i]+helper(i+2)
            skip=helper(i+1)

            total=max(buy,skip)
            cache[i]=total
            return total
        
        return (helper(0))
