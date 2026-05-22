class MinStack:
    

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.smallest=0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.stack)==1):
            self.smallest=val
        else:
            self.smallest=min(self.smallest,val)
        self.minStack.append(self.smallest)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if(len(self.minStack)>0):
            self.smallest=self.minStack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
