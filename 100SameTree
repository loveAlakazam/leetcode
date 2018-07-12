int Search(struct TreeNode * root1, struct TreeNode * root2){
    struct TreeNode * t1= root1;
    struct TreeNode * t2= root2;
    
    if(t1 !=NULL && t2!=NULL)
    {
        if(t1->val != t2->val) return 0;           
        else
        {
            if(Search(t1->left, t2->left)!=0)
            {
                if( Search(t1->right, t2->right)!=0) return 1;
                else return 0;
            }
            else return 0;
        }    
    } 
    else if (t1 ==NULL  && t2==NULL) return 1;
    else return 0;
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    int result = Search(p,q);
    if (result==1) return true;
    else return false;
}
