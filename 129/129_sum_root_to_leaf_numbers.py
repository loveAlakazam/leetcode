# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nums=[]
        
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, result):
            if node: #node가 존재
                if (node.left is None)and (node.right is None):#leaf노드
                    self.nums.append(int(result+str(node.val)))
                
                else:#말단노드가 아니라면
                    dfs(node.left, result+str(node.val))#왼쪽서브트리
                    dfs(node.right,result+str(node.val))#오른쪽서브트리
        
        dfs(root,'')
        return sum(self.nums)
