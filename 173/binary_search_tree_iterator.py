# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.elements=[]
        self.root= root
        def inorder(root):#중위순회
            if root:
                inorder(root.left)
                self.elements.append(root.val)
                inorder(root.right)
        inorder(self.root)
        self.elements.sort(reverse=True)#역순..
                
            
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        tmp= self.elements.pop()
        return tmp    
       

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.elements)>0:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
