class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums=sorted(nums)

        def check(diff):
            i=0
            count=0
            while i < len(nums)-1:
                if nums[i+1]-nums[i]<=diff:
                    i+=2
                    count+=1
                else:
                    i+=1
                
                if count>=p:
                    return True

            return False
            
        left=0
        right=nums[-1]-nums[0]
        ans=right

        while right>=left:
            mid=(right+left)//2
            if check(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        
        return ans

