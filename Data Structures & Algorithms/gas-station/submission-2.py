class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        total=0
        result=0

        
        for i in range(result,len(gas)):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                result=i+1

        if result==len(gas):
            return 0
        else:
            return result