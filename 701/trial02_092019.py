# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insertion(pre,now,key,origin_root):
            if now is None and pre is None:#비어있는 트리
                return TreeNode(key) #새로운 노드를 만들어서 리턴.
            
            else:
                if now:
                    pre=now
                    if now.val>key:
                        return insertion(pre,now.left,key,origin_root)
                    else:# now.val<key
                        return insertion(pre,now.right,key,origin_root)
                
                else:#root 가 None pre(선행노드)의 값과 비교하여 왼쪽/오른쪽 자식으로 선택=> 노드생성해서 삽입
                    if pre.val>key:
                        #노드를 생성해서 넣는다.
                        pre.left=TreeNode(key)
    
                    else:#pre.val<key
                        #노드를 생성해서 넣는다.
                        pre.right=TreeNode(key)
            return origin_root # origin_root는 root원본이다.
        now,origin_root=root,root
        x=insertion(None,now,val,origin_root)
        return x
