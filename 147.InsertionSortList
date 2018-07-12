#define SWAP(x,y,t) ( (t)=(x), (x)=(y), (y)=(t))
void insertion_sort(int * arr, int n);
int countNode (struct ListNode * head);
struct ListNode * isLast (struct ListNode * head);

struct ListNode* insertionSortList(struct ListNode* head) {
    
     struct ListNode * end = isLast(head); //last Node
    struct ListNode * i,*j,*k,*temp;
    if(head==NULL || head->next ==NULL) //노드를 갖지 않는 리스트 & 노드 원소가 1개인 리스트
        return head;
    else // (head !=NULL && head->next !=NULL) , 노드 원소가 2개이상인 리스트 
    {
         //노드의 개수를 탐색한다.
        int n = countNode(head); //마지막 노드 개수까지 고려..
    
        //노드 개수만큼의 배열을 생성한다
        struct ListNode * end = isLast(head), * p;
        int arr[n], i;
        
        //각 배열의 원소에 노드값들을 담는다.    
            for(p=head, i=0; p!=NULL && i<n ;p=p->next)
                arr[i++]=p->val;
    
    
        //insert_sort를 이용해서 배열원소를 정렬시킨다.
        insertion_sort(arr,n);
    
      //새로운 리스트를 만들어서 정렬시킨 원소를 넣는다...
          for(p=head,i=0; p!=NULL&& i<n ; p=p->next)
                p->val=arr[i++];
         return head;
    }   
}


void insertion_sort(int * arr, int n)
{
    int i,j,temp;
    for(i=1;i<n;i++){
        for(j=0;j<i;j++){
            if(arr[i]<arr[j])SWAP(arr[i],arr[j],temp);
        }
    }
}

int countNode(struct ListNode * head){
    struct ListNode * p =head;
    int n=0; //노드의 개수
    while(p!=NULL) {
        n++;
        p=p->next;
    }
    return n;
}

struct ListNode * isLast(struct ListNode * head){
    struct ListNode * p =head;
    while(p!=NULL) p=p->next;
    return p;
}
