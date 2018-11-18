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
	    //정렬
	    while(left<right)
        {
		    while(nums[left]!=val&& left<=numsSize-1){ //nums[left]!=val이면 left는 +1증가시킨다. 
			    left ++; 
		    } 
	
            //반면 nums[left]=val이면 멈춘다.
		    while(nums[right]==val&& right>=0){
			    right--;//nums[right]=val이면 right는 -1감소시킨다.
		    } 						 
		    
            //반면 nums[right]!=val이면 멈춘다.
            if(nums[left]!= nums[right] && left<right)
		        SWAP(nums[left],nums[right],temp);
		    left++;right--;					  
	    }
	
	    //정렬후 마지막 val이 아닌 값의 인덱스 번호를 찾는다  
	    int length;	//length: 처음으로 값이 val인 인덱스번호 
	    for(i=0;nums[i]!=val;i++);
	    length=i;
	    return length;
    } 
}
