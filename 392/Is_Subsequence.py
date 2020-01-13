class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for se in s:
            idx= t.find(se)
            if idx==-1:
                return False
            else:
                t=t[idx+1:]
        return True
