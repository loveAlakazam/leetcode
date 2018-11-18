from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one_num=[]
        cnt= Counter(nums)
        for key in cnt:
            if cnt[key]==1:
                one_num.append(key)
        if len(one_num)==1:
            return one_num[0]
        else: #len(one_num)!=1
            return 0
