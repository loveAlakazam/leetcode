void merge(int *nums, int left, int mid, int right);
void merge_sort(int*nums, int left, int right);
int missingNumber(int* nums, int numsSize) {
    int i;
    merge_sort(nums,0,numsSize-1);
    int lastMember = nums[numsSize-1];
    int original[numsSize+1];
    for(i=0;i<=lastMember;i++)
        original[i]=i;

    for(i=0; i<numsSize  ;i++)
    {
        if(original[i]!=nums[i])return original[i];
    }
    return lastMember+1;
}

void merge_sort(int*nums, int left, int right){
    if(left<right){
        int mid = (left+right)/2;
        merge_sort(nums,left,mid);
        merge_sort(nums,mid+1,right);
        merge(nums,left,mid,right);
    }
}

void merge(int *nums, int left, int mid, int right){ 

    int b1=left, e1=mid; //part-list 1
    int b2=mid+1, e2=right;//part-list 2
    int new_arr[right+1]; //ordered list
    int now_index = left;
    while(b1<=e1 && b2<=e2){
        if(nums[b1]<nums[b2])
            new_arr[now_index]=nums[b1++];
        else //nums[b1]>=nums[b2]
            new_arr[now_index]=nums[b2++];
        now_index++;
    }
    int i;
    if(b1>e1) {
        for(i=b2;i<=e2;i++)
           new_arr[now_index++] = nums[i]; 
    }
    else {// b2>e2
        for(i=b1;i<=e1;i++)
           new_arr[now_index++] = nums[i]; 
    }
    for(i=left;i<=right;i++)
        nums[i] = new_arr[i];
}
