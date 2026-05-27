class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2

        if(len(nums)==1):
            return nums[0]
            
        while left<right:
            mid=(left+right)//2
            if(nums[mid]>nums[right]):
                left=mid+1
            elif(nums[mid]<=nums[right]):
                right=mid
        
        return nums[left]
