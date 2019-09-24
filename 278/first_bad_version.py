# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right= 1, n
        while(left<right):
            mid=(left+right)//2
            
            if isBadVersion(mid) is False:
                left= mid+1
            
            else: #isBadVersion(mid) is True
                right=mid
        
        # left ==right
        if isBadVersion(left) is True:
            return left
        return -1
