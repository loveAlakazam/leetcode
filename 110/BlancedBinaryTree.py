# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 트리의 높이를 구하는 함수.
        def get_height( root:TreeNode) ->int:
            if root is None: 
                return 0
            return 1+max(get_height(root.left), get_height(root.right))
        
        if root is None:
            return True
        
        left_height=get_height(root.left)
        right_height=get_height(root.right)
        
        return (abs(left_height-right_height) <=1 and self.isBalanced(root.left) and self.isBalanced(root.right))
