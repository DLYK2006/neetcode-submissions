class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums=nums
        self.cache=[0]*len(nums)
        self.helper(0)
        return self.cache[0]

    def helper(self,i):
        if i>len(self.nums)-1:
            return 0
        if self.cache[i]!=0:
            return self.cache[i]
        self.cache[i]=max(self.nums[i]+self.helper(i+2),self.helper(i+1))
        return self.cache[i]