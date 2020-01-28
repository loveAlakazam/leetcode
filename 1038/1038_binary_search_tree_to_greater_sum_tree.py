# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 합순서: 오른쪽서브트리 -> 자기자신 -> 왼쪽서브트리
        self.prevSum=0 #이전합
        self.root=root
        return self.makeSum(root)
        
    
    def makeSum(self, node):
        #현재 노드가 존재하면
        if node:
            #오른쪽서브트리 부터 합을 구한다
            self.makeSum(node.right)
            
            # 오른쪽서브트리 합에 노드 자기자신을 더한다
            # prevSum을 업데이트한다.
            self.prevSum += node.val
            
            #현재 노드의 val값을 수정해야한다.
            node.val= self.prevSum
            
            #왼쪽서브트리로 이동한다.
            self.makeSum(node.left)
        
        # 루트를 반환한다.
        return self.root
        
    
