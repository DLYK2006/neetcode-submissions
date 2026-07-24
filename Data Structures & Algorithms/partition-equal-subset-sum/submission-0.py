class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        half=sum(nums)/2
        cache={}

        def helper(i,curSum):
            if curSum==half:
                return True
            
            if i==len(nums) or curSum > half:
                return False

            if (i, curSum) in cache:
                return cache[(i, curSum)]
                    
            result = helper(i + 1, curSum + nums[i]) or helper(i + 1, curSum)
            
            cache[(i, curSum)] = result
            return result

        return helper(0,0)
        