class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(digit):
            sum=0
            for i in range(len(digit)):
                sum+=int(digit[i])**2
            return sum
        seen=set()
        digit=str(n)
        while helper(digit)!=1:
            print(seen)
            if helper(digit) in seen:
                return False
            seen.add(helper(digit))
            digit=str(helper(digit))
        return True
            
