from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.grah=defaultdict(list)   

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.grah[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result=""
        if key not in self.grah:
            return result
        time=[data[1] for data in self.grah[key]]
        left=0
        right=len(time)-1
        mid=(left+right)//2
        while right>=left:
            if timestamp>=time[mid]:
                result=self.grah[key][mid][0]
                left=mid+1
                mid=(left+right)//2
            elif timestamp<time[mid]:
                right=mid-1
                mid=(left+right)//2     
        return result  

        