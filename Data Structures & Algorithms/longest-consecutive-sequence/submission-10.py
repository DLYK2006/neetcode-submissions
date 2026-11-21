class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        highest=0
        numbers=set(nums)
        
        for i in nums:
            if i-1 not in numbers:
                start=i
                grah=1
                while start+1 in numbers:
                    grah+=1
                    start+=1
                highest=max(grah,highest)
        
        return highest

                

                
                
        