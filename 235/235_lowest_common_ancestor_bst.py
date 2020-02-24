# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, pq):
            if root.val>pq.val:#왼쪽서브트리
                return -1
            return 1 #오른쪽서브트리
                    
                    
        def dfs(root, p, q):
            if root: #루트노드 존재
                #p,q가 서로 다른 트리에 있는가?
                if search(root,p)!=search(root,q):
                    return root
                
                else:
                    #root가 p또는 q와 같은가?
                    if (root.val==p.val) or (root.val==q.val):
                        return root
                    #p,q가 왼쪽서브트리에있다
                    elif root.val>p.val:
                        return dfs(root.left,p,q)
                    return dfs(root.right,p,q)
                
        return dfs(root,p,q)
