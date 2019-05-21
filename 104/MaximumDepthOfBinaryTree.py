# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: #루트가 가리키는 노드가 존재하지 않는다 => 높이 0
            return 0
        
        #루트가 존재한다=> 왼쪽서브트리의 높이 와 오른쪽서브트리의 높이 중 가장 큰 값을 선택 
        # 현재 노드(root가 가리키는 노드) 
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))  
