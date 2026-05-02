class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        product=1
        output=[]
        for i in range(length):
            product=1
            for m in range(length):
                if(m==i):
                    continue 
                product*=nums[m]
            output.append(product)
        
        return output
                