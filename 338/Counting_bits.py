class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        binaries=[]
        for i in range(0,num+1): # 1~num
            binaries.append(bin(i)[1:].count('1'))
        return binaries
