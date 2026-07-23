class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=nums[0]
        result=nums[0]

        for i in range(1,len(nums)):
            tempMax=maxi
            tempMini=mini

            maxi=max(nums[i],tempMax*nums[i],tempMini*nums[i])
            mini=min(nums[i],tempMini*nums[i],tempMax*nums[i])

            result=max(maxi,mini,result)
        
        return result