int even(char * s, int length){
	int last= length-1; //null���� �ٷ����� �ε���
	int m=last/2,same=0, i; //m�� last/2�� �ش��ϴ� �ε���, same: �糡 ������ Ȯ���ϴ� ī��Ʈ��ȣ 
	for(i=0; i<=m; i++){
		if(s[i]==s[last-i])
			same++;
	}
	return same;
}

int odd(char * s, int length){

	int last= length-1; //null���� �ٷ����� �ε���
	int m=last/2,same=0, i; //m�� last/2�� �ش��ϴ� �ε���, same: �糡 ������ Ȯ���ϴ� ī��Ʈ��ȣ 
	for(i=0; i<m; i++){
		if(s[i]==s[last-i])
			same++;
	}
	return same;
}

bool isPalindrome(int x){
	//1. ���� ==> ���ڿ� 
	    char s[12];
	    sprintf(s,"%d",x);
	//2. null���ڸ� ã�Ƽ� ������ ������ ���Ѵ�.
	    int null_index; //null���� �ε�����ȣ
	    int i;
	    for(i=0; s[i]!='\0';i++);
	        null_index=i;  //null���� �ε��� ��ȣ�� ã��
	//���ڼ� =null���� �ε��� ��ȣ 
	    int length = null_index; 

	//3-1. ���ڼ��� ¦���� ��
	    int same;
	    if(length%2==0)
		    same=even(s, length);
	//3-2. ���ڼ��� Ȧ���� ��
	    else //length%2 !=0
		    same=odd(s, length);
	
	if(same==length/2) return true;
	else return false;	
}
