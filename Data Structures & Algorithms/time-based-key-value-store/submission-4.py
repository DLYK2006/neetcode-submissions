class TimeMap:

    def __init__(self):
        self.mood={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mood:
            self.mood[key]=[(value,timestamp)]
        else:
            self.mood[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mood:
            return ""
        left=0
        right=len(self.mood[key])-1
        mid=(left+right)//2
        result=""
        while left<=right:
            mid=(left+right)//2
            if(self.mood[key][mid][1]==timestamp):
                return self.mood[key][mid][0]
            elif(self.mood[key][mid][1]<timestamp):
                result=self.mood[key][mid][0]
                left=mid+1
            else:
                right=mid-1
        return result
            