class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        freq={1:0, 2:0}
        #target을 홀수로한다
        #만일 짝수의개수가 홀수보다 크다면 나중에 target=2로 변경된다.
        target=1
        
        #짝수의 개수(freq[2])와 홀수의 개수(freq[1])를 카운트
        for chip in chips:
            if chip%2==0:
                freq[2]+=1
            else:
                freq[1]+=1
        
        if freq[2]>freq[1]:
            target=2
        
        cost=0
        for chip in chips:
            diff= abs(chip-target)
            # diff(chip-target)%2==1 => 1차이 난다 -> cost=1듦
            if diff%2==1:
                cost+=1
        return cost
