
bool hasCycle(struct ListNode *head) {
    struct ListNode * t = head; //현재
    if(head==NULL) return false; //비어있는 리스트 : cycle 아님
    else{//비어있지 않은 리스트
        while(t->next !=NULL){
            
              t->val = -1000;
              t=t->next; 
              if(t->val ==-1000) return true;
        }
        return false; //t가 NULL
    }
}
