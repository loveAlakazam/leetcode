class Solution:
    def arrangeCoins(self, n: int) -> int:
        level=1
        result=0
        while level<=n:
            result=level
            n-=level
            level+=1
            
        return result

    # level=1, n=5, result=0 => level<n (o)=> result=1, n=4, level=2
    # level=2, n=4, result=1 => level<n (o)=> result=2, n=2, level=3
    # level=3, n=2, result=2 => level>n(x) => return result=2
    
    # level=1, result=0, n=8 => level(1)<n(8)=> result=1, n=7, level=2
    # level=2, result=1, n=7 => level(2)<n(7)=> result=2, n=5, level=3
    # level=3, result=2, n=5 => level(3)<n(5)=> result=3, n=2, level=4
    # level=4, result=3, n=2 => level>n (x) => return result=3
    
    # level=1, n=0,  result=0 => level(1)<n(0) => 
        
