class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp=[False]*(len(nums)+1)
        dp[0]=True

        if len(nums)>=2:
            dp[2]=(nums[1]==nums[0])

        for i in range(3,len(nums)+1):
            if dp[i-2] and nums[i-2]==nums[i-1]:
                dp[i]=True
            
            elif dp[i-3] and nums[i-3]==nums[i-1]==nums[i-2]:
                dp[i]=True
            
            elif dp[i-3] and (nums[i - 2] == nums[i - 3] + 1 and nums[i - 1] == nums[i - 2] + 1):
                dp[i]=True
        
        return dp[len(nums)]

        pass
