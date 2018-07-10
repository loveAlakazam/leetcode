int even(char * s, int length){
	int last= length-1; //null문자 바로이전 인덱스
	int m=last/2,same=0, i; //m은 last/2에 해당하는 인덱스, same: 양끝 같은지 확인하는 카운트번호 
	for(i=0; i<=m; i++){
		if(s[i]==s[last-i])
			same++;
	}
	return same;
}

int odd(char * s, int length){

	int last= length-1; //null문자 바로이전 인덱스
	int m=last/2,same=0, i; //m은 last/2에 해당하는 인덱스, same: 양끝 같은지 확인하는 카운트번호 
	for(i=0; i<m; i++){
		if(s[i]==s[last-i])
			same++;
	}
	return same;
}

bool isPalindrome(int x){
	//1. 정수 ==> 문자열 
	    char s[12];
	    sprintf(s,"%d",x);
	//2. null문자를 찾아서 글자의 개수를 구한다.
	    int null_index; //null문자 인덱스번호
	    int i;
	    for(i=0; s[i]!='\0';i++);
	        null_index=i;  //null문자 인덱스 번호를 찾음
	//글자수 =null문자 인덱스 번호 
	    int length = null_index; 

	//3-1. 글자수가 짝수일 때
	    int same;
	    if(length%2==0)
		    same=even(s, length);
	//3-2. 글자수가 홀수일 때
	    else //length%2 !=0
		    same=odd(s, length);
	
	if(same==length/2) return true;
	else return false;	
}
