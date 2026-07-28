class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}

        def helper(i,target):
            if target==0 and i==len(nums):
                return 1

            if i==len(nums):
                return 0

            if (i,target)in cache:
                return cache[(i,target)]
            
            add=helper(i+1,target-nums[i])
            minus=helper(i+1,target+nums[i])
            
            result=add+minus
            cache[(i,target)]=result
            return cache[(i,target)]
        
        return helper(0,target)