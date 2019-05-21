# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans=[]
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root: #루트가 가리키는 노드가 존재한다면
            #왼쪽 서브트리를 먼저 탐색
            self.postorderTraversal(root.left)
            
            #오른쪽 서브트리를 먼저 탐색
            self.postorderTraversal(root.right)
            
            #나를 읽는다
            self.ans.append(root.val)
            
        return self.ans
