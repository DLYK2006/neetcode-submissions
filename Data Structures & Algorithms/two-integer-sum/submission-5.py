

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers={}
        
        for i in range(len(nums)):
            numbers[nums[i]]=i
        
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in numbers and i!=numbers[temp]:
                return [i,numbers[temp]]


        