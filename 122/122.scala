object Solution {
    def maxProfit(prices: Array[Int]): Int = {
        var sum=0
        var result=0
        for(i<- 1 until prices.length){
            result=prices(i)-prices(i-1)
            if (result>0)
                sum+=result
        }
        sum
    }
}
