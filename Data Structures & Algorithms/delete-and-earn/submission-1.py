class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        highest=max(nums)
        totalpoints=[0]*(highest+1)

        for i in nums:
            totalpoints[i]+=i

        dp=[0]*(highest+1)
        dp[0]=totalpoints[0]
        dp[1]=max(totalpoints[0],totalpoints[1])

        for i in range(2,highest+1):
            take=totalpoints[i]+dp[i-2]
            skip=dp[i-1]
            dp[i]=max(skip,take)
        
        return dp[highest]