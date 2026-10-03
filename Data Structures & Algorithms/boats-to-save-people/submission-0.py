class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        l=0
        r=len(people)-1
        people=sorted(people)
        
        while r>=l:
            weight=people[l]+people[r]

            if weight<=limit:
                boats+=1
                l+=1
                r-=1
            elif weight>limit:
                boats+=1
                r-=1
        if r==l:
            boats+=1
        return boats

