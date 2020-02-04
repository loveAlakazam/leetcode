class Solution:
    
    # 배열 A의 원소중 음수인 원소(최대K개)를 
    # 양수로 바꾼다.
    def minus2Plus(self ,A, K, minus_idx):
        for iidx, i in enumerate(minus_idx, start=1):
            if iidx<=K and A[i]<0:
                A[i]= A[i]*(-1)
                K-=1
        return A,K
                
        
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        lena= len(A)
        while K>0:
            #A를 오름차순 정렬
            A=sorted(A)
            
            #음수개수 카운트
            minus_idx=[]
            for i in range(lena):
                if A[i]<0:
                    minus_idx.append(i)
            
            # 음수가 한개이상있다면..
            # -1을 한번 곱하여 음수를 양수로 전환
            minus_cnt=len(minus_idx)
            if minus_cnt>0:
                A,K= self.minus2Plus(A,K, minus_idx)
            
            #음수가 더이상 없다면
            #제일작은수에 (-1)**K 를 곱한다.
            else:# minus_cnt==0
                A[0]=A[0]*((-1)**K)
                K=0
                
        return sum(A)
