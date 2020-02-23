# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sums=[]
        
    def dfs(self, node, sum):
        if node:
            #만일 리프노드라면
            if (node.left is None) and (node.right is None):
                self.sums.append(sum+node.val)
            
            #왼쪽서브트리
            self.dfs(node.left, sum+node.val)
                
            #오른쪽서브트리
            self.dfs(node.right,sum+node.val) 
            
            
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: #루트가 존재하지 않으면 False로 함.
            return False
        
        self.dfs(root, 0)
        
        #중복을 막기위해서 list->set으로 변환
        self.sums=set(self.sums)
        if sum in self.sums:
            return True
        return False
