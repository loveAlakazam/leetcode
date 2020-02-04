# -*- coding: utf-8 -*-
# leetcode.1005. references
import sys
class Solution:
    def largestSumAfterKNegations(self, A, K):
        S=sorted(A)
        i=0
        val=0
        while K>0:
            if S[i]<0:
                S[i]= -S[i]
                K-=1
                i+=1
            else:
                if i==0 or S[i]<abs(S[i-1]):
                    S[i]=-S[i]
                else:
                    S[i-1]=-S[i-1]
                K-=1
            return sum(S)
        
def main():
    s=Solution()
    T=int(sys.stdin.readline())
    for _ in range(T):
        A=list(map(int, sys.stdin.readline().split()))
        K=int(sys.stdin.readline())
        result=s.largestSumAfterKNegations(A,K)
        print(result)

if __name__=='__main__':
    main()
