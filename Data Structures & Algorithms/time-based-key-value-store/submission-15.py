class TimeMap:

    def __init__(self):
        self.values=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        left=0
        right=len(self.values[key])-1

        while right>=left:
            mid=(right+left)//2
            if self.values[key][mid][0]==timestamp:
                return(self.values[key][mid][1])
            if self.values[key][mid][0]>timestamp:
                right=mid-1
            else:
                left=mid+1
        
        if right>=0:
            return(self.values[key][right][1])
        return ""


