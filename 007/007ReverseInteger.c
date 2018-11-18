int natural(int x){
    //1. 정수 ==> 문자열로 변환
        char changeChar[12]; //32bit정수는 10자리 수이므로
        sprintf(changeChar,"%u",x);
               
    //2. null문자의 인덱스를 찾는다. 
       int null_index;//null 문자의 index번호
	   int l; //changeChar의 문자 길이 
	   int i;
	   for(i=0;changeChar[i]!='\0'; i++);
	   null_index=i;
	   l= i+1;
	  
    //3. 거꾸로 배치
       char * reverse = (char *)malloc(sizeof(char)*l); //같은 길이 만큼 동적할당
	   for(i=0; i<=l-2; i++){
	   	 reverse[i]=changeChar[(l-2)-i];
	   } 
	   reverse[l-1]='\0'; //문자열의 마지막 index에 null삽입 
	 
	   
    //4-1. 문자열로 변환 중 정수가 될 수 있는 숫자의 범위에 벗어나면 return 0으로 한다.
	 int changeInt;
	 char * integerMAX="2147483648";
	 if(l==11){//null문자까지 합해서 11자리문자열(10자리수) 
	 	for(i=0;i<11;i++)
        {
	 		if(reverse[i]>integerMAX[i])
	 			return 0;
            else if(reverse[i]<integerMAX[i]){
	 			changeInt =atoi(reverse);
        		return changeInt;
			 }
		 }
	 }	
	
	 //4-2. 10자리수 문자열이 아니라면: 문자열 ==> 정수로 변환
		changeInt =atoi(reverse);
        return changeInt;
}

int reverse(int x) {
    int result;
    if(x>0){//양수
        result=natural(x);
    }
    else if(x==0) result= 0;
    else{//음수x<0
        //01. 입력수(x)에 -1을 곱한다.
        	x=x*-1;
        //02. 양수와 동일한 처리
            result=natural(x);
        //03. 02과정이 다되면 다시 -1을 곱함.
            result*=-1;   
    }
    return result;
}
