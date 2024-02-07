class MinStack:

    def __init__(self):
        self.list=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.list.append(val)
        if self.min==[] or val<=self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        peek=self.list.pop()
        if peek==self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()