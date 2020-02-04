object Solution {
    def isvalid(lcnt:Int, rcnt:Int):Boolean={
            if(lcnt==rcnt){
                return true
            }
            return false
    }
    
    def balancedStringSplit(s: String): Int = {
        
        
        var result=0
        var lcnt=0
        var rcnt=0
        
        for(x <- s){
            if (x equals 'L'){lcnt+=1}
            
            else{rcnt+=1}
            
            if (isvalid(lcnt,rcnt))
            {
                    result+=1
                    lcnt=0
                    rcnt=0
            }
        }
        return result
    }
}
