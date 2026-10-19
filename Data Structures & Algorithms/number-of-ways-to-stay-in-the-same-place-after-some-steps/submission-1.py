class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        cache={}

        def helper(step,pos):
            if step==0 and pos==0:
                return 1
            elif step==0 and pos!=0:
                return 0                
            if pos==arrLen or pos<0:
                return 0
            if (step,pos) in cache:
                return cache[(step,pos)]
            
            result=0
            left=helper(step-1,pos-1)
            right=helper(step-1,pos+1)
            stay=helper(step-1,pos)

            result=(left+right+stay)%1000000007
            cache[(step,pos)]=result
            return result

        return (helper(steps,0))





        pass
