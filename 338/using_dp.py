class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        binaries=[]
        # 작은 곳에서 큰곳으로
        for i in range(0,num+1):
            if i<=1:
                binaries.append(i)
            else: #i>=2
                # 마지막 숫자가 0인가?
                if i%2==0:
                    binaries.append(binaries[i>>1])
                # 마지막 숫자가 1인가?
                else:
                    binaries.append(binaries[i>>1]+1)        
        return binaries
