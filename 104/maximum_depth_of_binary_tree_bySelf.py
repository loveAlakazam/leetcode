# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        
        if root.val!=None and root.left==None and root.right==None:
            return 1
        
        L=self.maxDepth(root.left)
        R=self.maxDepth(root.right)
        if L==R:
            return 1+L
        return 1+max(L,R)
