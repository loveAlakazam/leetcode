# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer=0
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):
            if node:#현재노드가 존재
                left_length=dfs(node.left) #왼쪽
                right_length=dfs(node.right)#오른쪽
                
                left_arrow=right_arrow=0
                
                if node.left and node.left.val==node.val:
                    left_arrow= left_length+1
                
                if node.right and node.right.val==node.val:
                    right_arrow=right_length+1
                    
                self.answer=max(self.answer, left_arrow+ right_arrow)
                return max(left_arrow, right_arrow)
            return 0
        
        dfs(node=root) #탐색
        return self.answer
