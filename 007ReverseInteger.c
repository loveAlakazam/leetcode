int natural(int x){
    //1. ���� ==> ���ڿ��� ��ȯ
        char changeChar[12]; //32bit������ 10�ڸ� ���̹Ƿ�
        sprintf(changeChar,"%u",x);
               
    //2. null������ �ε����� ã�´�. 
       int null_index;//null ������ index��ȣ
	   int l; //changeChar�� ���� ���� 
	   int i;
	   for(i=0;changeChar[i]!='\0'; i++);
	   null_index=i;
	   l= i+1;
	  
    //3. �Ųٷ� ��ġ
       char * reverse = (char *)malloc(sizeof(char)*l); //���� ���� ��ŭ �����Ҵ�
	   for(i=0; i<=l-2; i++){
	   	 reverse[i]=changeChar[(l-2)-i];
	   } 
	   reverse[l-1]='\0'; //���ڿ��� ������ index�� null���� 
	 
	   
    //4-1. ���ڿ��� ��ȯ �� ������ �� �� �ִ� ������ ������ ����� return 0���� �Ѵ�.
	 int changeInt;
	 char * integerMAX="2147483648";
	 if(l==11){//null���ڱ��� ���ؼ� 11�ڸ����ڿ�(10�ڸ���) 
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
	
	 //4-2. 10�ڸ��� ���ڿ��� �ƴ϶��: ���ڿ� ==> ������ ��ȯ
		changeInt =atoi(reverse);
        return changeInt;
}

int reverse(int x) {
    int result;
    if(x>0){//���
        result=natural(x);
    }
    else if(x==0) result= 0;
    else{//����x<0
        //01. �Է¼�(x)�� -1�� ���Ѵ�.
        	x=x*-1;
        //02. ����� ������ ó��
            result=natural(x);
        //03. 02������ �ٵǸ� �ٽ� -1�� ����.
            result*=-1;   
    }
    return result;
}
