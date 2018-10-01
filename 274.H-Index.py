# https://leetcode.com/problems/h-index/description/
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations)==0:
            return 0
        
        citations.sort(reverse=True)
        for c in range(len(citations)):
            if c >= citations[c]:
                return c
        return c+1
