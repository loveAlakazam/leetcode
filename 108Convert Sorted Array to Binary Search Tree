/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void insert_treeNode(struct TreeNode ** root, int key)
{
    struct TreeNode * p =NULL;  //부모 노드
    struct TreeNode * t =*root;  //현재 노드
    struct TreeNode * n;         //삽입 시킬 노드
 
    while(t!=NULL){ //탐색한다.
       // if(key= t->val) return ; //key값이 트리에 이미 존재
        p=t; 
        if(p->val < key) t= p->right;
        else t=p->left;   //(p->val >=key)
        }

    //key값을 갖는 노드가 트리에 없으므로 key값을 갖는 노드를 추가한다.
    n=(struct TreeNode *) malloc(sizeof (struct TreeNode)); //동적메모리할당
    if (n==NULL)return;
    n->val = key ;
    n->left = n->right = NULL;

    if(p!= NULL){ //비어있지 않은 트리라면
        if(p->val < key) p->right = n;
        else p->left = n;
    } 
    else *root=n;//비어 있는 트리라면..
}

struct TreeNode * merge(int* nums, struct TreeNode * root, int left, int right)
{
    int mid;
    if(left<=right){
        mid = (left+right)/2;
        insert_treeNode(&root,nums[mid]);
        merge(nums,root,left,mid-1);
        merge(nums,root,mid+1,right);
    }
    
    return root;
}


struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {    
    struct TreeNode * root = NULL;
    //전체 트리 루트노드를 중심으로, [루트보다 작은 집합] 루트 [루트보다 큰 집합] 에서
    root =merge(nums,root,0,numsSize-1);
    return root;
}
