class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        frequency=defaultdict(int)
        left=0
        right=0
        currmax=0
        highest=0

        for right in range(len(nums)):
            currmax+=nums[right]
            frequency[nums[right]]+=1

            if right-left+1 >k:
                frequency[nums[left]]-=1
                if frequency[nums[left]]==0:
                    del frequency[nums[left]]
                currmax-=nums[left]
                left+=1
                    
            if right-left+1==k and len(frequency)==k:
                highest=max(currmax,highest)
        
        return highest

        


        pass
