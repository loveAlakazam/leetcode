#(문제) 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #왼쪽 서브트리 노드들 중 최댓값을 찾는 함수(가장 오른쪽노드)
        def find_max_value(root, max_left):
            if root is not None:
                if root.right is None:
                    return max_left
                
                #root.right is not None
                max_left=max(max_left, root.right.val)
                return find_max_value(root.right, max_left)
            
            # root is None
            return max_left
            

        #오른쪽 서브트리 노들 중 최솟값을 찾는 함수(가장왼쪽노드)
        def find_min_value(root, min_right):
            if root is not None:
                if root.left is None:
                    return min_right
                
                #root.left is not None
                min_right=min(root.left.val, min_right)
                return find_min_value(root.left, min_right)
                
            # root is None
            return min_right
            
        #########################################
        #root 노드가 존재하지 않는다면
        if root is None:
            return True
        if root is not None:
            #1.root만 존재
            if root.left is None and root.right is None:
                return True
            
            #2.왼쪽 서브트리만 존재 (참조건: 왼쪽서브트리 최댓값< root.val)
            if root.left is not None and root.right is None:
                max_left= find_max_value(root.left, root.left.val)
                if root.val > max_left:
                    return True
                else: return False
            
            #3.오른쪽 서브트리만 존재(참조건: 오른쪽서브트리 최솟값>root.val)
            if root.right is not None and root.left is None:
                min_right=find_min_value(root.right, root.right.val)
                if root.val < min_right:
                    return True
                else: return False
            
            #4. 양쪽 트리 모두 존재(참조건: 왼쪽서브트리 최댓값< root.val< 오른쪽 서브트리 최솟값)
            if root.left is not None and root.right is not None:
                max_left=find_max_value(root.left, root.left.val)
                min_right=find_min_value(root.right, root.right.val)
                if root.val> max_left and root.val < min_right:
                    return True
                else:
                    return False
            
            
