class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers=defaultdict(int)
        
        for i in range(len(nums)):
            numbers[nums[i]]=i
        
        for i in range(len(nums)):
            wow=target-nums[i]
            if wow in numbers and i!=numbers[wow]:
                return [i,numbers[wow]]
