class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result=''.join( list(map(lambda x: x if x in J else '',S)))
        return len(result)
