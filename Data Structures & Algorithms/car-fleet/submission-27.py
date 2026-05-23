class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        timeTakenS=[]
        fleets=0

        for position,speed in cars:
            timeTakenS.append((target-position)/speed)
        
        print(timeTakenS)
        

        lastFleetTime = 0  

        for t in timeTakenS:
            if t > lastFleetTime:
                fleets += 1
                lastFleetTime = t
                        
        return fleets
