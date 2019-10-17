class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        end_cnt=[0]*(N+1)
        start_cnt=[0]*(N+1)
        for start, end in trust:
            start_cnt[start]+=1
            end_cnt[end]+=1
        
        for i in range(1,N+1):
            if end_cnt[i]==N-1 and start_cnt[i]==0:
                return i
        return -1
