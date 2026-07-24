class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache={}

        def helper(i,j):
            if len(nums)==i:
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            include=0
            if j==-1 or nums[i]>nums[j]:
                include=helper(i+1,i)+1
            exclude=helper(i+1,j)

            result=max(include,exclude)
            cache[(i,j)]=result
            return result
        
        return helper(0,-1)

        
        
        
