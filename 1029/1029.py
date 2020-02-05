class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result=0
        # cost[i][0]와 cost[i][1]의 차이의 절댓값을 기준으로 내림차순 정렬한다.
        costs=sorted(costs, key=lambda x:abs(x[0]-x[1]), reverse=True)
        
        acnt=0
        bcnt=0
        # 지원자수 2N= len(costs) (리스트의 row 개수)
        # N= len(costs)//2
        N=len(costs)//2 
        for cost in costs:
            if acnt<N and bcnt<N:
                result+=min(cost)
                
                # A가 B보다 싸다
                if cost[0]<cost[1]:
                    acnt+=1
                    
                # B가 A보다 싸다.
                else:# cost[0]>=cost[1]
                    bcnt+=1
            
            elif acnt==N:# i번째 사람은 자동으로 B로 이동
                result+=cost[1]
                bcnt+=1
                
            elif bcnt==N:#i번째 사람은 자동으로 A로 이동
                result+=cost[0]
                acnt+=1
            
        return result
        
