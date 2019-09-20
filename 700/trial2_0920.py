# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search_key(root, key):
            if root:
                if root.val==key:
                    return root
                elif key<root.val:
                    return search_key(root.left, key)
                elif key>root.val:
                    return search_key(root.right, key)
            return None
                
        return search_key(root,val)
