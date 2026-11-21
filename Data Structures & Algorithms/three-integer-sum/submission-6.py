class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            a=nums[i]
            if a>0:
                break
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while r>l:
                three=a+nums[l]+nums[r]
                if three==0:
                    result.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif three>0:
                    r-=1
                elif three<0:
                    l+=1
        return result
        