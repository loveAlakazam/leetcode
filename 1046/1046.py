class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones의 길이가 1이될때까지 반복문 진행
        while len(stones)>1:
            #내림차순정렬
            stones=sorted(stones, reverse=True)
            
            if stones[0]>stones[1]:
                #0번째돌(큰돌)은 1번째돌을 뺀 나머지값으로 바뀐다.
                stones[0]-=stones[1]
                
                #1번째 돌은 없어진다
                stones.pop(1)
                
            #같으면 두개다 없어짐
            elif stones[0]==stones[1]:
                for _ in range(2):
                    #맨앞에 있는돌 2개를 차례로 없앤다
                    stones.pop(0)
                    
        #만약에 남은 돌이 없다면 0을 리턴
        if len(stones)==0:
            return 0
        return stones[0]
