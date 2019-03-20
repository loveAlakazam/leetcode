# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def are_keys_in_range(root, 
                              low_range=float('-inf'),
                             high_range=float('inf')):
            if not root:
                return True
            elif not low_range < root.val < high_range:
                return False
            return (are_keys_in_range( root.left, low_range, root.val) and are_keys_in_range(root.right, root.val, high_range))
        return are_keys_in_range(root)
