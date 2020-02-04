# -*- coding: utf-8 -*-
import sys

class Solution:
    def minus2Plus(self,A,K, minus_idx):
        # iidx의 start를 1로 시작한다.
        # 최대 K개의 음수를 양수로 바꾼다.
        for iidx,  i in enumerate(minus_idx, start=1):
            if iidx<=K and  A[i]<0:
                A[i]=A[i]*(-1)
                K-=1
        return A,K

    def largestSumAfterKNegations(self, A, K):
        while K>0:
            #A를 오름차순 정렬
            A=sorted(A)
            print('현재 A: ', A)
            print('현재 K: ', K)

            #A의 음수개수 카운트
            minus_idx=[]
            for i in range(len(A)):
                if A[i]<0:
                    minus_idx.append(i)
                    
            minus_cnt=len(minus_idx)
            print('음수개수: ', minus_cnt, minus_idx)
        
            #음수가 1개이상이면
            #음수를 양수로 전환
            if minus_cnt>0:
                A,K= self.minus2Plus(A,K, minus_idx )

            # 음수가 더이상 없다면..
            # 제일작은 수에다가 (-1)**K를 곱한다.
            else:
                A[0]=A[0]*(-1)**K
                K=0
            print()
        print(A)
        print(sum(A))
        return sum(A)

def main():
    print('테스트케이스 개수: ')
    T=int(sys.stdin.readline())
    s=Solution()
    for t in range(T):
        A=list(map(int, sys.stdin.readline().split()))
        K=int(sys.stdin.readline())
        result=s.largestSumAfterKNegations(A,K)
        print(result)
        
if __name__=="__main__":
    main()
