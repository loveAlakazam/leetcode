int square(int n){
    return n*n;
}

int TenDivider(int sum, int n){
    if(n<10){
        sum+=n*n;
        return sum;
    }
    else{
        sum+=square(n%10);
        return TenDivider(sum,n/10);
    }
}

int distinct(int sum, int n){
    int result=TenDivider(sum,n);
    if(result<10) return result;
    else return distinct(0,result);
}

bool isHappy(int n) {
    int sum=0;
    
    if (distinct(0,n)==1 || distinct(0,n)==7) return true;
    else return false;

}
