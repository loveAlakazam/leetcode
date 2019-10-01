class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N<=1:
            return N
        else:
            left,right=0,1
            for i in range(2,N+1):
                tmp=right
                right=tmp+left
                left=tmp
            return right
