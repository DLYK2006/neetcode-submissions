class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        
        if(len(nums)==1):
            if(target==nums[0]):
                return 0
            else:
                return -1

        while left<right:
            mid=(left+right)//2
            if(nums[mid]==target):
                return mid
        
            if(nums[mid]>nums[left]):
                if(target>=nums[left] and target<nums[mid]):
                    right=mid
                else:
                    left=mid+1
            elif(nums[mid]<=nums[left]):
                if(nums[mid]==nums[left]):
                    left = mid + 1
                if(target>=nums[mid] and target<=nums[right]):
                    left=mid+1
                else:
                    right=mid
            if nums[left] == target:
                return left
        return -1

