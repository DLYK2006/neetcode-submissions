class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache={}

        def helper(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==len(nums):
                return 0 
            include=0
            if j==-1 or nums[i]>nums[j]:
                include=helper(i+1,i)+1
            skip=helper(i+1,j)
            result=max(skip,include)
            cache[(i,j)]=result
            return result
        
        return(helper(0,-1))
            
            