class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while right>left:
            pivot=(right+left)//2
            if nums[pivot]>nums[right]:
                left=pivot+1
            else:
                right=pivot
            if nums[pivot]==target:
                return pivot
        pivot=left

        if nums[-1]>=target>=nums[pivot]:
            left=pivot
            right=len(nums)-1
        else:
            right=pivot
            left=0
        
        while right>=left:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        
        return -1
            
