class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sexy=set()
        highest=[]
        for i in nums:
            if i not in sexy:
                sexy.add(i)
            else:
                continue

        for i in sexy:
            if(i-1 in sexy):
                continue
            else:
                max=1
                while i+1 in sexy:
                    max+=1
                    i+=1
            highest.append(max)
        
        highest.sort()
        print(highest)
        if len(highest)==0:
            return 0
        else:
            return highest[-1]