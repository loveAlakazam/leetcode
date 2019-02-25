class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 or K==1:
            return 0
        
        if K<=2**(N-2):
            return self.kthGrammar(N-1,K)
        
        else:#K>2**(N-2)
            return 1^self.kthGrammar(N,K-2**(N-2))
