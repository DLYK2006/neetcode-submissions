class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)
        target=total-x

        if total<x:
            return -1
        length=-1
        left=0
        right=0
        window=0

        while right<len(nums):
            window+=nums[right]
            right+=1
            while window>target:
                window-=nums[left]
                left+=1
            if window==target:
                length=max(length,right-left)

        if length==-1:
            return -1
        else:
            return len(nums)-length
        pass
