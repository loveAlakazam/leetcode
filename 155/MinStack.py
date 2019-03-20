class MinStack:
    # MinStack 클래스 생성자
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 스택생성 - 비어있는 리스트를 반환
        self.stack = []
        

    #메소드 push :원소 x를 넣는다.
    def push(self, x: int) -> None:
        self.stack.append(x)
  
    #메소드 pop: 맨위의 원소를 뺀다.
    def pop(self) -> None:
        if len(self.stack) >0:
            self.stack.pop()
        
    #메소드 top: 맨위의 원소를 빼지 않고 값만 확인
    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]
    #메소드 getMin :스택의 원소들 중 가장작은 원소를 찾는다.
    def getMin(self) -> int:
        if len(self.stack)>0:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
