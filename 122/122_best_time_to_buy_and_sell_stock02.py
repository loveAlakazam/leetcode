class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length= len(prices)
        if length<=1:
            return 0
        else:
            profits=[0]*(length-1)
            for i in range(length-1):
                profits[i]=prices[i+1]-prices[i]
            
            result=sum(p for p in profits if p>0)
            return result
