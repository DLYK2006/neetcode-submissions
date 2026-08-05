from collections import deque

class MinStack:

    def __init__(self):
        self.stack=deque()
        self.mins=deque()
        self.minimum=float('inf')        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins)>0:
            self.minimum=min(val,self.mins[-1])
        else:
            self.minimum=float('inf')
            self.minimum=min(val,self.minimum)
        self.mins.append(self.minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
