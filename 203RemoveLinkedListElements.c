/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    if(head==NULL)return head; //비어있는 리스트라면
    else //비어있지 않은 리스트
    {
        struct ListNode * p= head;   //탐색 포인터
        int targetNum=0;    //찾으려는 숫자의 개수 0으로 초기화
        
        //찾으려는 숫자(매개변수 val)의 개수를 구한다.
        while(p!=NULL)
        {
            if(p->val ==val)targetNum++;
            p=p->next;
        }
        if(targetNum ==0) //찾는 타겟 숫자가 리스트에 존재하지 않는다면 헤드포인터를 그대로 리턴
            return head;
        else //targetNum >1 
        {
            int i;
            struct ListNode* now;
            struct ListNode* front;
            if(head->val ==val && head->next==NULL)return NULL;
            
            for(i=1; i<=targetNum; i++)
            {
                now=head;
                front =NULL;
                while(now->val !=val){
                    front =now;
                    now= now->next;
                }
                //1. 맨 첫번째 노드가 val일 때
                if(now==head){
                    head=now->next; 
                }
                            
                //2. 맨 마지막 노드가 val일 때
                else if(now->next==NULL)
                    front->next=NULL;
                            
                //3. 중간에 속하는 노드가 val일 때 (맨처음, 맨끝이 아닌 노드)
                else{
                    front->next=now->next;
                }        
            }
             return head;
        }
    } 
}
