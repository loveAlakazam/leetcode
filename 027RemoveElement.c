#define SWAP(x,y,t) ( (t)=(x), (x)=(y) , (y)=(t) )
int removeElement(int * nums, int numsSize, int val){
    if(numsSize==0)return 0;
    int i, same=0;
    for(i=0;i<numsSize;i++)
        if(nums[i]==val) same++;
    if(same==numsSize)return 0;
    else if(same==0) return numsSize;
    else
    {
        
	    int left=0 , right= numsSize-1;
	    int temp;
	    //����
	    while(left<right)
        {
		    while(nums[left]!=val&& left<=numsSize-1){ //nums[left]!=val�̸� left�� +1������Ų��. 
			    left ++; 
		    } 
	
            //�ݸ� nums[left]=val�̸� �����.
		    while(nums[right]==val&& right>=0){
			    right--;//nums[right]=val�̸� right�� -1���ҽ�Ų��.
		    } 						 
		    
            //�ݸ� nums[right]!=val�̸� �����.
            if(nums[left]!= nums[right] && left<right)
		        SWAP(nums[left],nums[right],temp);
		    left++;right--;					  
	    }
	
	    //������ ������ val�� �ƴ� ���� �ε��� ��ȣ�� ã�´�  
	    int length;	//length: ó������ ���� val�� �ε�����ȣ 
	    for(i=0;nums[i]!=val;i++);
	    length=i;
	    return length;
    } 
}
