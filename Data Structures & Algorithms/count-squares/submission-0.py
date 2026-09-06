from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.coords=defaultdict(int)

    def add(self, point: List[int]) -> None:
        x=point[0]
        y=point[1]
        self.coords[(x,y)]+=1
        

    def count(self, point: List[int]) -> int:
        square=0
        for key in self.coords:
            if key[0]!=point[0] and key[1]!=point[1]:
                cod1=(point[0],key[1])
                cod2=(key[0],point[1])
                if cod1 in self.coords and cod2 in self.coords:
                    square+=(self.coords[cod1])*(self.coords[cod2])*self.coords[key]
        return square
                