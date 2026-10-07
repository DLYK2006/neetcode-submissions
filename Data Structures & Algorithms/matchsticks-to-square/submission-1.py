class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        target=sum(matchsticks)/4
        matchsticks.sort(reverse=True)

        if matchsticks[0]>target:
            return False

        sides = [0] * 4

        def helper(i):

            if i == len(matchsticks) and (sides[0] == sides[1] == sides[2] == sides[3]):
                return True

            for j in range(4):
                if sides[j]+matchsticks[i]<=target:
                    sides[j]+=matchsticks[i]
                
                    if helper(i+1):
                        return True
                    sides[j]-=matchsticks[i]
                
                if sides[j]==0:
                    break

            return False


        return helper(0)
