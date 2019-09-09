class Solution:
    def reverse(self, x: int) -> int:
        numToString= list(str(x))
        numToString= ''.join(numToString[::-1])
        
        if(x<0):#음수
            result=int(numToString[-1]+numToString[:-1])
        else:#양수
            result= int(numToString)
        
        # reversed된 숫자가 32비트 범위를 넘는다면 0으로한다.
        if( result<-(2**31) or result>=(2**31)):
            return 0
        return result
