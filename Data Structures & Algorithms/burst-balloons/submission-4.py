class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache={}
        nums.append(1)
        nums.insert(0,1)

        def helper(l,r):
            if (l,r) in cache:
                return cache[(l,r)]

            if l>r:
                return 0
            
            maxc=0

            for i in range(l+1,r):
                
                total=helper(l,i)+helper(i,r)+(nums[l]*nums[i]*nums[r])
            
                maxc=max(total,maxc)
            cache[(l,r)]=maxc
            return maxc
        
        return helper(0,len(nums)-1)
            
