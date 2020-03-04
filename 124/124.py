# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_val=float('-inf')
        
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPathDown(node):
            if node is None:
                return 0
            left=max(0, maxPathDown(node.left))
            right=max(0, maxPathDown(node.right))
            self.max_val= max(self.max_val, left+right+node.val)
            return max(left,right)+node.val
        
        maxPathDown(root)
        return self.max_val
