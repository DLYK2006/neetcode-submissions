class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        index=len(nums)-2
        while index!=-1:
            if nums[index]>=goal-index:
                goal=index
            index-=1
        
        if goal==0:
            return True
        else:
            return False
