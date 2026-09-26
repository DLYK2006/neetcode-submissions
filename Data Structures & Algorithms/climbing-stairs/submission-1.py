class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}

        def helper(i):
            if i==n:
                return 1
            elif i>n:
                return 0
            if i in cache:
                return cache[i]
            result=0
            result=helper(i+1)+helper(i+2)
            cache[i]=result
            return result
        
        return helper(0)
