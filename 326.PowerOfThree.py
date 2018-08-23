import math
class Solution:
    def isPowerOfThree(self, n):
        if n==0:
            return False
        k=0
        num=1
        while(1):
            num=math.pow(3,k) #3^k
            if num>=n:
                break
            k+=1
        if num==n:
            return True
        else:
            return False
