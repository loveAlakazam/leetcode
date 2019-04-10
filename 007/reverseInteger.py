class Solution:
    def reverse(self, x: int) -> int:
        result=None
        # 초기 x가 음수인가?
        if x<0:
            result=list(str(x)[1:])[::-1]
            result=int(''.join(result))*-1
            
        # 초기 x가 양수인가?
        elif x>=0:
            result=list(str(x))[::-1]
            result=int(''.join(result))
            
        # result=reverse(x) 가 -(2**31)< result<(2**31)-1 인가?
        if -(2**31)<= result<2**31:
            return result
        
        return 0
