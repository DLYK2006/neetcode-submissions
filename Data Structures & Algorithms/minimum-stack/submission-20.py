class MinStack:

    def __init__(self):
        self.stack=deque()
        self.minimum=[]
        self.index=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.index==0:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val,self.minimum[self.index-1]))
        self.index+=1

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        self.index-=1
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[self.index-1]
