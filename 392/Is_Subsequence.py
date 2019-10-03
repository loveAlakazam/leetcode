class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result=[-1]*len(s) #-1로 모두 초기화
        t_start_idx=0
        for idx,se in enumerate(s):
            tmp =t[t_start_idx:]
            if se in tmp:# 부분리스트 tmp에 se가 있다면
                result[idx]=t_start_idx+tmp.index(se)
                t_start_idx= result[idx]+1 #tmp에서 se를 발견한인덱스+1을 다음탐색 시작점으로한다.
            else: #se가 tmp에 없다
                return False
            
        # 다있는데 순서가 오름차순순이냐를 확인
        if sorted(result)!=result: # 뒤에원소가 앞에원소보다 작다면
            return False
        return True
