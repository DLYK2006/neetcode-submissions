class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexes=deque()
        left=0
        right=0
        output=[]


        while right<len(nums):
            
            while indexes and (nums[right]>nums[indexes[-1]]):
                indexes.pop()
            indexes.append(right)

            if(left==right-k+1):
                output.append(nums[indexes[0]])
                if(left in indexes):
                    indexes.remove(left)
                left+=1

            right+=1

        return output