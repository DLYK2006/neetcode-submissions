class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid=int(len(nums)/2)
        left=0
        right=len(nums)-1
        while left<=right:
            if(target!=nums[mid]):
                if(target<nums[mid]):
                    right=mid-1
                    mid=int((left+right)/2)
                elif(target>nums[mid]):
                    left=mid+1
                    mid=int((left+right)/2) 
            if(target==nums[mid]):
                return mid
        return -1
        