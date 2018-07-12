#define SWAP(x,y,t) ( (t)=(x), (x)=(y), (y)=(t))
void quickSort(int*nums,int left, int right);
int partition(int*list,int left, int right);

int find_overlap(int *nums, int numsSize){
    int i, overlap=0;
    for(i=0;i<numsSize-1;i++){
        if(nums[i]==nums[i+1])
            overlap++;
    }
    return overlap;    
}

int thirdMax(int* nums, int numsSize)
{
    int i; //RnumsSize is the number of real-elements
    //to sort elements
    quickSort(nums,0,numsSize-1);
    //1. to find overlap count
    int overlap=find_overlap(nums,numsSize);
    if(overlap>0)//to get rid of the overlap elements
    {
        int realNum = numsSize-overlap;
    
        //to input  the array arr(real elements group)  elements
        int arr[realNum];
        int j=0;
        for(i=0;i<numsSize ;i++){
            if(nums[i]!=nums[i+1] && j<realNum){
                arr[j++]=nums[i];
            }
        } 
   
     //find the 3rd maximum (if the number of the real-elements is less than 3, return maximum element)
        if(realNum<3) return arr[realNum-1];
        else return arr[realNum-3];
    }
    
    else //none overlap
    {
        if(numsSize<3)return nums[numsSize-1];
        else return nums[numsSize-3];
    }
}

//Order Statics : QuickSort
//quick
int partition(int *list ,int left, int right)
{
    int pivot =list[left], low=left, high=right+1, temp;
    do{
        do{
            low++;
        }while(low<=right && list[low]<=pivot);
        
        do{
            high--;
        }while(high>=left && list[high]>pivot);
        
        if(low<high)SWAP(list[low],list[high],temp);
    }while(low<high);
    SWAP(list[left],list[high],temp);
    return high;
}

void quickSort(int *nums, int left, int right){
    if(left<right){
        int q= partition(nums,left,right); //pivot's position
        quickSort(nums,left,q-1);
        quickSort(nums,q+1,right);
    }
}

