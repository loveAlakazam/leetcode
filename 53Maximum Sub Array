int maxSubArray(int* nums, int numsSize) {
    int sumStorage[numsSize];
    int sum= 0;
    int max;
    int i,j;
    for(i=0; i<numsSize; i++){
        sum +=nums[i];
        if(nums[i]>sum){
            sum = nums[i];
            sumStorage[i]=sum;
        }
        sumStorage[i]=sum;    
    }
    
    max= sumStorage[0];
    for(i=1;i<numsSize; i++)
        if(max<sumStorage[i]) max= sumStorage[i];
    return max;
}
