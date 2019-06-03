#url: https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def insert(now, val):
            if now is None: #루트가 가리키는 노드가 존재하지 않으면
                #val을 값으로 갖는 노드를 생성
                node=TreeNode(val)
                now = node
                return root

            else: #루트가 가리키는 노드가 존재하면
                if now.val > val:# now의 키값이 val보다 크다(새로 추가해야될 노드는 현재 노드의 왼쪽서브트리에 속한다.)
                    if now.left is None: #왼쪽 자식노드가 존재하지 않는다면
                        node= TreeNode(val)
                        now.left=node
                        return root

                    else: #왼쪽 자식노드가 존재한다면-> 왼쪽 서브트리탐색
                        return insert(now.left, val)

                else: #root의 키값이 val보다 작거나 같다(새로 추가해야될 노드는 현재 노드의 오른쪽 서브트리에 속한다.)
                    if now.right is None: #오른쪽 자식노드가 존재하지 않느다면
                        node= TreeNode(val)
                        now.right=node
                        return root
                    else:
                        return insert(now.right, val)
        return insert(root,val)
