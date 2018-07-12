/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var pl = prices.length; //array prices length
    var now_buying; //현재 구매가격
    var MaxProfit=0;
    var sub; //판매가격(prices[j]- now_selling)
    for(var i=0;i<pl-1; i++){
        now_buying = prices[i];
        for(var j=i; j<pl; j++){
            if(now_buying<prices[j]){
                sub= prices[j]- now_buying;
                if(sub>MaxProfit) MaxProfit = sub;
            }   
        }
    }
        
    return MaxProfit;
};
