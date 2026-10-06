class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, value: int) -> None:
        if not self.stack:
            res=value
        else:
            res=min(value,self.stack[-1][1])    
        res=min(res,value)
        self.stack.append([value,res])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()