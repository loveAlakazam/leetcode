class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lenp=len(prices)
        if lenp<=1:
            return 0
        
        # 내림차순 정렬로 되어있으면 어차피 profit=0
        if prices==sorted(prices,reverse=True):
            return 0
        
        min_price=float('inf') #무한대라고 가정
        max_profit=0
        for i in range(lenp):
            if(prices[i]<min_price):
                min_price=prices[i]
            elif prices[i]-min_price>max_profit:
                max_profit= prices[i]-min_price
        return max_profit
