# url: https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:#val을 탐색
        if root is None: #루트가 존재하지 않는다면
            return None
        
        else: #루트가 존재한다.
            #찾는값 val과 root의 값을 비교한다.
            if root.val == val:
                return root
            elif val< root.val: # val < root의 키값
                return self.searchBST(root.left, val) #왼쪽서브트리 탐색
            else: #val>=root.val
                return self.searchBST(root.right,val)
