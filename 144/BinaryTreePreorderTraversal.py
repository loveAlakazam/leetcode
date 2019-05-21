# url: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=[]
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:#루트가 가리키는 노드가 존재한다면
            #나를 먼저 읽는다
            self.ans.append(root.val)
            
            #왼쪽 서브트리를 읽는다
            self.preorderTraversal(root.left)
            
            #오른쪽 서브트리를 읽는다
            self.preorderTraversal(root.right)
        
        return self.ans
        
