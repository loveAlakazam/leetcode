class Solution:
    def isValance(self, lcnt, rcnt):
        if lcnt==rcnt:
            return True
        return False
        
    def balancedStringSplit(self, s: str) -> int:
        answer=0
        
        #lcnt: L 카운트
        #rcnt: R 카운트
        lcnt, rcnt=0,0
        for x in s:
            if x=='R':
                rcnt+=1
            else:# x=='L'
                lcnt+=1
            if self.isValance(lcnt, rcnt) is True:
                answer+=1
                lcnt, rcnt=0,0
        
        return answer
