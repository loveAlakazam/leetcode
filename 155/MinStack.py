class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 스택생성 - 비어있는 리스트를 반환
        self.stack = []
        

    #원소 x를 넣는다.
    def push(self, x: int) -> None:
        self.stack.append(x)
  
    #맨위의 원소를 뺀다.
    def pop(self) -> None:
        if len(self.stack) >0:
            self.stack.pop()
        
    #맨위의 원소를 빼지 않고 값만 확인
    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack)>0:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
