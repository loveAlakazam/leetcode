class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        result=[]
        for i in range(n+1): #i=0,1,...,n
            if i<2:
                result.append(1)
            else: #(i>=2) result[i]=result[i-1]+result[i-2]
                tmp = result[i-1]+result[i-2]
                result.append(tmp)
                
        return result[n]
