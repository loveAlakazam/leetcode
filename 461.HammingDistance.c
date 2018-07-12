#define BIG(x,y,s) (x>y)? (s=x): (s=y)
int makeSpace(int number,int space)
{
    if(number/2==0)return ++space;
    else{
        space++;
        return makeSpace(number/2,space);
    }
}

int hammingDistance(int x, int y) {
    //1. 비트공간 개수를 구한다. (크기가 큰 수의 비트공간의 개수만큼 확보. )
        int Xspace=0, Yspace=0;
        int space; 
        Xspace=makeSpace(x,Xspace);
        Yspace=makeSpace(y,Yspace);         
    
    //2. 데이터를 넣는다. (두 숫자의 비트공간 수가 서로 다를 때만)
      //비트 데이터 공간 개수 비교
        if(Xspace != Yspace) //비트 공간 개수가 서로 다른가?  
             BIG(Xspace,Yspace,space);  //더큰 비트 공간 개수로 space값을 넣음.
        else space = Xspace; //비트 공간 개수가 서로 같은 경우    
        
    //3. 이진수를 넣는다.
         int i;
         int * arrX = (int)malloc(sizeof(int)*space);
         int * arrY = (int)malloc(sizeof(int)*space);
         
         for(i=0;i<space;i++){
            arrX[i]=0;
            arrY[i]=0;
         }
         
         for(i=space-1; i>=0&& x!=1 ; i--){
                arrX[i]= x%2;
                 x/=2;
         }arrX[i]=x;
         
         for(i=space-1; i>=0&& y!=1 ; i--){
                arrY[i]= y%2;
                 y/=2;
         }arrY[i]=y;
         
    //4. 헤밍디스턴스
    int different=0;
    for(i=0; i<space; i++)
        if(arrX[i]!=arrY[i])
            different++;
    return different;
}
