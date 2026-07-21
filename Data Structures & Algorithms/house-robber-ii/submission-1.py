class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cache1=[-1]*len(nums)
        cache2=[-1]*len(nums)
        result=[]
        array1=nums[0:len(nums)-1]
        array2=nums[1:len(nums)]
        def dfs(i,cache,array):
            if i>=len(array):
                return 0
            if cache[i]!=-1:
                return cache[i]
            cache[i]=max(array[i]+dfs(i+2,cache,array),dfs(i+1,cache,array))
            return cache[i]
        
        ans1=dfs(0,cache1,array1)
        ans2=dfs(0,cache2,array2)
        
        return max(ans1,ans2)
        
            