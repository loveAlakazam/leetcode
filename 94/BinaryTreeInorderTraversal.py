# url: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=[] #비어있는 리스트 (노드가 None이 아닌 노드를 가리킨다.)
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            #왼쪽 서브트리를 먼저 본다
            self.inorderTraversal(root.left)
            
            #나를 읽는다.
            self.ans.append(root.val)
            
            #오른쪽 서브트리를 먼저본다
            self.inorderTraversal(root.right)
            
        #else root is None: #root가 가리키는 노드가 존재하지 않으면 
        return self.ans
